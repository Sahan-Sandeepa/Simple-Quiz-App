from quizmanager import QuizManager

class QuizApp:

    QUIZ_FOLDER = "Quizzes"

    def __init__(self):
        self.username = ""
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)
    
    def startup(self):
        #print the greeting at startup
        self.greeting()

        #ToDo : ask the user for their name
        self.username = input("What is your username? ")
        print(f"Welcome, {self.username}! ")
        print()
    
    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("-~-~-~-~-~-~-~-~-~-~Welcome to PyQuiz! -~-~-~-~-~-~-~-~-~-~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print()

    def menu_header(self):
        print("-------------------------")
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
        while(True):
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()

            if selection[0] == "E":
                self.goodbye()
                break
            if selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print("\nAvailable Quizzes Are: ")

                #ToDo list the quizzers
                self.qm.list_quizzes()

                print("--------------------------\n")
                continue

            elif selection[0] == "T":
                try:
                    quiznum = int(input("Quiz Number: "))
                    print(f"You have selected quiz {quiznum}")

                    #ToDo start the quiz

                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()

                    dosave = input("Save the rusults? (y/n): ")
                    dosave = dosave.capitalize()
                    if len(dosave) > 0 and dosave[0] == "Y":
                        self.qm.save_results()

                except:
                    self.menu_error()
                
                else:
                    self.menu_error()


    #This is the entry poin to the program

    def run(self):
        #execute the startup routine
        self.startup()
        #Start main program
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
