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
    
    def startElement(self, name, attrs):
        if name == "QuizML":
            self._parse_state == QuizParserState.PARSE_QUIZ
            self.new_quiz.name == attrs["name"]

    def endElement(self, name):
        if name == "QuizML":
            self._parse_state == QuizParserState.IDLE
        
        #ToDo: process the rest of the tags

    def characters(self, content):
        pass
    