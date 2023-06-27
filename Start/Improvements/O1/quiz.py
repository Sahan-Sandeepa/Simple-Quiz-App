import datetime
import sys
import random


class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.is_correct = False

    def print_header(self):
        print("\n\n*************************************")
        print(f"Quiz Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Questions: {self.questions}")
        print(f"Total Points: {self.total_points}")
        print("*****************************************\n")

    def print_result(self, quiztaker, thefile = sys.stdout):
        print("*************************************", file=thefile, flush=True)
        print(f"RESULTS For {quiztaker}", file=thefile, flush=True)
        print(f"Date: {datetime.datetime.today()}", file=thefile, flush=True)
        print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile, flush=True)
        print(f"SCORE: {self.score} points out of possible {self.total_points}", file=thefile, flush=True)
        print("*****************************************\n")

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for i in self.questions:
            i.is_correct = False
        self.print_header()
        
        random.shuffle(self.questions)
        
        for s in self.questions:
            s.ask()
            if s.is_correct:
                self.correct_count += 1
                self.score += s.points
        return self.score, self.correct_count, self.total_points


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")
            if len(response) == 0:
                print("Sorry, this is not a valid response! Please try again.")
                continue
            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("Sorry, this is not a valid response! Please try again.")
                continue
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestionMc(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while True:
            print(self.text)
            for i in self.answers:
                print(f"({i.name}) {i.text}")
            response = input("? ")
            if len(response) == 0:
                print("Sorry, this is not a valid response! Please try again.")
                continue
            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
