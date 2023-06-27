import os.path
import os
import quizparser
import datetime

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        self.the_quiz = None

        self.quizzes = dict()

        self.results = None

        self.quiztaker = ""

        if (os.path.exists(quizfolder) == False):
            raise FileNotFoundError("The Quiz Seems Not Exist!")
        self._buid_quiz_list()

    def _buid_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = quizparser.QuizParser()
                self.quizzes[i + 1] = parser.parse_quiz(f)

    def list_quizzes(self):
        for k, V in self.quizzes.items():
            print(f"({k}: {V.name})")

    def take_quiz(self, quizid, usename):
        pass

    def print_results(self):
        pass

    def save_results(self):
        pass

if __name__ == "__main__":
    qm = QuizManager("Quizzes")
    qm.list_quizzes()