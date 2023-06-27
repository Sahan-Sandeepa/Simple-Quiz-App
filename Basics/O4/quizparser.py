import xml.sax
from quiz import *
from Basics.O2.quiz import *
from enum import Enum, unique

@unique
class QuizParserState(Enum):
    
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5

class QuizParser(xml.sax.ContentHandler):

    """
    The QuizParser class loads a paticular quiz file, parses it and return 
    fully-built quiz object that can then be presented to the user.

    """
    def __init__(self):
        self.new_quiz = Quiz()

        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quizpath):
        #load the file content

        with open(quizpath, "r") as quizfile:
            if quizfile.mode == "r":
                quiztext = quizfile.read()
        xml.sax.parseString(quiztext, self)

        #return the finished quiz
        return self.new_quiz
    
    def startElement(self, tagname, attrs):

        if tagname == "QuizML":
            self._parse_state == QuizParserState.PARSE_QUIZ
            self.new_quiz.name == attrs["name"]

        elif tagname == "Description":
            self._parse_state == QuizParserState.PARSE_DESCRIPTION

        elif tagname == "Question":
            self._parse_state = QuizParserState.PARSE_QUESTION
            if attrs["type"] == "multichoice":
                self._current_question = QuestionMc()
            elif attrs["type"] == "tf":
                self._current_question == QuestionTF()
            self._current_question.points = int(attrs["points"])
            self.new_quiz.total_points += self._current_question.points

        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUEST_TEXT
            self._current_question.correct_answer = attrs["answer"]
            
        elif tagname == "Answer":
            self._current_answer = Answer()
            self._current_answer.name = attrs["name"]
            self._parse_state = QuizParserState.PARSE_ANSWER

    def endElement(self, tagname):

        if tagname == "QuizML":
            self._parse_state == QuizParserState.IDLE
        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tagname == "Question":
            self.new_quiz.questions.append(self._current_question)
            self._parse_state = QuizParserState.PARSE_QUIZ  
        #ToDo: process the rest of the tags
        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUESTION
        elif tagname == "Answer":
            self._current_question.answers.append(self._current_answer)
            self._parse_state = QuizParserState.PARSE_QUESTION

    def characters(self, chars):

        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += chars
        elif self._parse_state == QuizParserState.PARSE_QUEST_TEXT:
            self._current_question.text += chars

if __name__ == "__main__":
    app = QuizParser()
    qz = app.parse_quiz("Quizzers/SampleQuiz.xml")
    print(qz.name)
    print(qz.description)
    print(len(qz.questions))
    print(qz.total_points)
    for q in qz.questions:
        print(q.text)
    