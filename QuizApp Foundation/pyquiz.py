class QuizApp:
    def __init__(self):
        self.username = ""
    
    def startup(self):
        #print the greeting at startup
        self.greeting()

        #ToDo : ask the user for their name
    
    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("-~-~-~-~-~-~-~-~-~-~Welcome to PyQuiz! -~-~-~-~-~-~-~-~-~-~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print()

    def menu_header(self):
        print("------------------------------------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")