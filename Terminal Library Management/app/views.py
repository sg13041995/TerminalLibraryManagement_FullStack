from os import system

class View:
    def __init__(self):
        pass
    
    # initial greet on start of the applicaion
    def greet_user(self):
        print("//////////////////////////////////////////////////////////////")
        print("///////// Welcome to the Terminal Library Management /////////")
        print("//////////////////////////////////////////////////////////////")
    
    # exit greet when user quits the application
    def exit_greet(self):
        print("TLM> Quiting the application...")
        print("//////////////////////////////////////////////////////////////")
        print("//////////// Thank you for using the application /////////////")
        print("//////////////////////////////////////////////////////////////")
    
    # role menu display, selection and return
    def select_role_menu(self):
        print("\nPlease select a role:")
        print("(a) Client")
        print("(b) Librarian")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    # display the entered value and corresponding option if any
    def display_selection(self,option, role):
        print(f"TLM> You have selected '{option}' => '{role}'")
    
    # authentication menu display, selection and return
    def authentication_menu(self):
        print("\nPlease select an option:")
        print("(a) Signup")
        print("(b) Login")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    # display signup form and take input from the user for the form
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
    
    # display submission menu for the authentication form and return the selected option to the controller
    def form_submission_menu(self):
        print("\nPlease select an option:")
        print("(a) Submit")
        print("(b) Cancel")
        print("(c) Exit")
        print("Enter a or b or c")
        
        selected_option = input("TLM> ")
        return selected_option
    
    # if there is some error in the user input for the form then display the input field where user has made the mistake or form validity failed
    def signup_form_error(self, invalid_input_list : list) -> None:
        print("TLM> Invalid form input")
        print(f"TLM> Error in {list(i[0] for i in invalid_input_list)} input fields")
        print("Please try again...")
    
    # message on successful signup
    def signup_successful(self):
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////// Signup Successful //////////////////////")
        print("//////////////////////////////////////////////////////////////")
        
    # message on signup failure
    def signup_failed(self):
        print("//////////////////////////////////////////////////////////////")
        print("//////////////////////// Signup Failed ///////////////////////")
        print("//////////////////////////////////////////////////////////////")
    
    # authentication menu display, selection and return
    def auth_menu_after_signup(self):
        print("\nPlease select an option:")
        print("(a) Login")
        print("(b) Exit")
        print("Enter a or b")
        
        selected_option = input("TLM> ")
        return selected_option