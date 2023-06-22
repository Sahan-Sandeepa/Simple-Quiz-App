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

    def menu_error(self):
        print("That is not a valid selection. Please try again.")
    
    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print(f"Thank for using PyQuiz, {self.username}! ")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

    def menu(self):
        self.menu_header()

        #Run untill the user select the exit selection

        selection = ""

    #This is the entry poin to the program

    def run(self):

        #execute the startup routine
        self.startup()
        #Start main program
        self.main()

if __name__ = "__main__":
    app = QuizApp()
    app.run()

