from pyqtfive.utils import clear_screen, buffer

class Caya:
    def __init__(self):
        self.name = "Karl Christian M. Caya"
        self.age = 20
        self.band = "Wave to Earth"

    def greet(self):
        print(f"Hello, I'm {self.name}.")

    def show_age(self):
        print(f"I am {self.age} years old.")

    def favorite_band(self):
        print(f"My favorite band is {self.band}.")

    def double_age(self):
        print(f"My age doubled is {self.age * 2}.")

    def initials(self):
        print("Initials: KCMC.")

    def menu(self):
        while True:
            clear_screen()
            print("\n--- Hello, Welcome to Caya Menu ---")
            print("1. Greet")
            print("2. Show Age")
            print("3. Favorite Band")
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
                    self.favorite_band()
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