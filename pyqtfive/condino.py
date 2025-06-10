from pyqtfive.utils import buffer, clear_screen

class Condino:
    EXIT_OPTION = "0"
    UNSET_OPTION = "-1"

    def __init__(self):
        self.name = "Ciara Marie Condino"
        self.age = 21
        self.section = "BSIT 2-1"
        
    def show_name(self):
        print(f"Hi! I'm {self.name}.")

    def show_age(self):
        print(f"I am {self.age} years old.")

    def show_section(self):
        print(f"My section is {self.section}.")

    def show_hobby(self):
        print("My hobby is playing online games")

    def favorite_language(self):
        print("Python because of Sir Steven.")

    def menu(self):
        clear_screen()
        choice = self.UNSET_OPTION

        while choice != self.EXIT_OPTION:
            choice = self.display_get_choice()
            self.process_choice(choice)
            clear_screen()

    def display_get_choice(self):
        print("\n--- Condino's Menu ---")
        print("1. Greet")
        print("2. Show Age")
        print("3. Show Section")
        print("4. Hobby")
        print("5. Favorite Language")
        print("6. Back to Main Menu")

        return int(input("Enter your choice: "))

    def process_choice(self, choice):
        clear_screen()
        match choice:
            case 1:
                self.show_name()
            case 2:
                self.show_age()
            case 3:
                self.show_section()
            case 4:
                self.show_hobby()
            case 5:
                self.favorite_language()
            case 0:
                pass  # Exit to main menu
            case _:
                print("Invalid choice. Try again.")
                buffer()