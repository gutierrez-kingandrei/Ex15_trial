from pyqtfive.utils import clear_screen, buffer

class Caya:
    EXIT_OPTION = "0"
    UNSET_OPTION = "-1"
    
    def __init__(self):
        self.name = "Karl Christian M. Caya"
        self.age = 20
        self.band = "Wave to Earth"
        
    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.EXIT_OPTION:
            choice = self.display_get_choice()
            self.process_choice(choice)
            clear_screen()
            
    def display_get_choice(self):
        print("\n--- Hello, Welcome to Caya Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Favorite Band")
        print("4. Double Age")
        print("5. Initials")
        print("0. Back to Main Menu")

        return input("\nEnter your choice: ")
    
    def process_choice(self, choice):
        clear_screen()
        match choice:
            case "1":
                self.greet()
            case "2":
                self.show_age()
            case "3":
                self.favorite_band()
            case "4":
                self.double_age()
            case "5":
                self.initials()
            case "0":
                pass
            case _:
                print("Invalid choice.")
                
        buffer()
        
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