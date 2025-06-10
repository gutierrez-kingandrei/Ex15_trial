#Import modules from pyqtfive package
#TODO (ARGUELLES): Import a class from a module inside a package
from pyqtfive.caya import Caya 
from pyqtfive.condino import Condino 
#TODO (CORDOVA): Import a class from a module inside a package
from pyqtfive.gutierrez import Gutierrez

gutierrez = Gutierrez()
condino = Condino()
caya = Caya()

while True:
    print("=== Team Member Menu ===")
    print("1 - Norlan Arguelles")
    print("2 - Karl Caya")
    print("3 - Ciara Marie Condino")
    print("4 - Aron Stephen Cordova")
    print("5 - King Andrei Gutierrez")
    print("6 - Exit")
    
    choice = input("\nSelect a team member: ")
    
    match choice:
        case "1":
            #TODO (ARGUELLES): Call the appropriate function here
            pass
        case "2":
            caya.menu()
        case "3":
            condino.menu()
        case "4":
            #TODO (CORDOVA): Call the appropriate function here
            pass 
        case "5":
            gutierrez.menu()
        case "6":
            break   
        case _:
            print("Invalid choice. Please try again.")