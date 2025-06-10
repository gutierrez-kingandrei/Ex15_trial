from pyqtfive.utils import clear_screen, buffer

class Gutierrez:
    def __init__(self):
        self.name = "King Andrei Gutierrez"
        self.age = 20
        self.game = "Wuthering Waves"

    def greet(self):
        print(f"Hello, I'm {self.name}.")

    def show_age(self):
        print(f"I am {self.age} years old.")

    def favorite_game(self):
        print(f"My favorite online game is {self.game}.")

    def double_age(self):
        print(f"My age doubled is {self.age * 2}.")

    def initials(self):
        print("Initials: KAG.")

    def menu(self):
        while True:
            clear_screen()
            print("\n--- Hello, Welcome to Gutierrez Menu ---")
            print("1. Greet")
            print("2. Show Age")
            print("3. Favorite Language")
            print("4. Double Age")
            print("5. Initials")
            print("7. Back to Main Menu")

            choice = input("\nChoose an option: ")

            match choice:
                case "1":
                    self.greet()
                    buffer()
                case "2":
                    self.show_age()
                    buffer()
                case "3":
                    self.favorite_game()
                    buffer()
                case "4":
                    self.double_age()
                    buffer()
                case "5":
                    self.initials()
                    buffer()
                case "7":
                    break
                case _:
                    print("Invalid choice.")
                    buffer()

