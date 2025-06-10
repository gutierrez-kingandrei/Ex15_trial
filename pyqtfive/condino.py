class Condino:
    def __init__(self):
        self.name = "Condino, Ciara Marie M."
        self.age = 20
        self.section = "BSIT 2-1"

    def greet(self):
        print(f"Hello! I'm {self.name}.")

    def show_age(self):
        print(f"My age is {self.age}.")

    def show_section(self):
        print(f"My section is {self.section}.")

    def hobby(self):
        print("I enjoy coding and playing Grow a garden.")

    def favorite_language(self):
        print("My favorite programming language is Python.")

    def menu(self):
        while True:
            print("\n--- Condino's Menu ---")
            print("1. Greet")
            print("2. Show Age")
            print("3. Show section")
            print("4. Hobby")
            print("5. Favorite Language")
            print("6. Back to Main Menu")
            choice = input("Choose an option: ")
            
            match choice:
                case "1":
                    self.greet()
                case "2":
                    self.show_age()
                case "3":
                    self.show_section()
                case "4":
                    self.hobby()
                case "5":
                    self.favorite_language()
                case "6":
                    break   
                case _:
                    print("Invalid choice. Please try again.")
