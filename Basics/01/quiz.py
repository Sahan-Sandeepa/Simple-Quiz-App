class Question:
    def __init__(self):
         #ToDo: define the question field
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


