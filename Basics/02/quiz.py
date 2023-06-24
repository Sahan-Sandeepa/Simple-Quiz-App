
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

        #ToDo: print the quiz header
        print(f"Quiz Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Questions: {self.questions}")
        print(f"Total Points: {self.total_points}")
        print("*****************************************\n")

    def print_result(self):
        print("*************************************")

        print("*****************************************\n")

    def take_quiz(self):
        #ToDo: initialize the quiz state
        self.score = 0
        self.correct_count = 0
        for i in self.questions:
            i.is_correct = False
        #ToDo: print the header
        self.print_header()
        #ToDo: execute the each question and record the result
        for s in self.questions:
            s.ask()
            if (s.is_correct):
                self.correct_count += 1
                self.score += s.points 

        #ToDo: return the result
        return(self.score, self.correct_count, self.total_points)

class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

        #ToDo: define the ask method

    def ask(self):
        while(True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            #ToDo: if no response was entered
            if len(response) == 0:
                print("Sorry this is not the valid response!. Please try again.")
                continue

            #ToDo: check the either T or F given
            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("Sorry this is not the valid response!. Please try again.")
                continue           

            #Mark the answer as corrrect, if answer is same as the answer
            if response[0] == self.correct_answer:
                self.is_correct = True

            break

class QuestionMc(Question):
    def __init__(self):
        super().__init__()
        #ToDo: define the answer
        self.answers = []

    def ask(self):
        while(True):

            print(self.text)
            for i in self.answers:
                print(f"({i.name}) {i.text}")
            response = input("? ")

            if len(response) == 0:
                print("Sorry this is not the valid response!. Please try again.")
                continue

            response = response.lower()

            if response[0] == self.correct_answer:
                self.is_correct = True

            break

class Answer:
    def __init__(self):
        pass
        self.text = ""
        self.name = ""