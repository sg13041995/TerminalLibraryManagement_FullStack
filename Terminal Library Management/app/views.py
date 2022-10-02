from os import system

class View:
    def __init__(self):
        pass
    
    def greet_user(self):
        print("//////////////////////////////////////////////////////////////")
        print("///////// Welcome to the Terminal Library Management /////////")
        print("//////////////////////////////////////////////////////////////")
    
    def select_role_menu(self):
        print("\nPlease select a role:")
        print("(a) Client")
        print("(b) Librarian")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    def display_selection(self,option, role):
        print(f"TLM> You have selected '{option}' => '{role}'")
        
    def authentication_menu(self):
        print("\nPlease select an option:")
        print("(a) Login")
        print("(b) Signup")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    def exit_greet(self):
        print("TLM> Quiting the application...")
        print("//////////////////////////////////////////////////////////////")
        print("//////////// Thank you for using the application /////////////")
        print("//////////////////////////////////////////////////////////////")