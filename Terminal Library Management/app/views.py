from os import system

class View:
    def __init__(self):
        pass
    
    def greet_user(self):
        print("//////////////////////////////////////////////////////////////")
        print("///////// Welcome to the Terminal Library Management /////////")
        print("//////////////////////////////////////////////////////////////")
    
    def exit_greet(self):
        print("TLM> Quiting the application...")
        print("//////////////////////////////////////////////////////////////")
        print("//////////// Thank you for using the application /////////////")
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
        print("(a) Signup")
        print("(b) Login")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    def signup_form(self):
        user_signup_dict = {}
        
        print("\nPlease enter the following details to signup:")
        user_signup_dict["fname"] = input("TLM> First Name: ")
        user_signup_dict["lname"] = input("TLM> Last Name: ")
        user_signup_dict["email"] = input("TLM> Email: ")
        user_signup_dict["pass1"] = input("TLM> Password: ")
        user_signup_dict["pass2"] = input("TLM> Re-enter Password: ")
        user_signup_dict["ph"] = input("TLM> Phone Number: ")

        return user_signup_dict
    
    def form_submission_menu(self):
        print("\nPlease select an option:")
        print("(a) Submit")
        print("(b) Cancel")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
        
    
    def signup_form_error(self, invalid_input_list : list) -> None:
        print("TLM> Invalid form input")
        print(f"TLM> Error in {list(i[0] for i in invalid_input_list)} input fields")
        print("Please try again...")