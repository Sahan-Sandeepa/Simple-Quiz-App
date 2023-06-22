class Question:
    def __init__(self):
         #ToDo: define the question field
         self.points = 0
         

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

        #ToDo: define the ask method

    def ask(self):
        while(True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            #ToDo: if no response was entered

