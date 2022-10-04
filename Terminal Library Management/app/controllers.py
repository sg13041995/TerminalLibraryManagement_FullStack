from app.models import Model
from app.views import View
# validator module holds the functions for validating the individual input fields of the form
from app import validator

class Controller:
    def __init__(self, view: View, model: Model):
        # model holds the object of Model class
        self.model = model
        # view holds the object of View class
        self.view = view
    
    # entry point of application
    def start_application_handler(self) -> None:
        self.view.greet_user()
    
    # exit the application
    def exit_application_handler(self):
        self.view.exit_greet()
        exit()
    
    # helps to display the menu for role and authentication
    # screen=1 -> role
    # screen=2 -> authentication
    # screen=3 -> signup
    def menu_display_handler(self, fa, fb, fc, a, b, c, role=True, screen=1):
        selected_option = ''
        selected_option_name = ''
        
        while ((selected_option != 'a') or (selected_option != 'b') or (selected_option != 'c')):
            if (screen == 1):
                selected_option = self.view.select_role_menu()
            elif (screen == 2):
                selected_option = self.view.authentication_menu()
            elif (screen == 3):
                selected_option = self.view.form_submission_menu()
            
            if selected_option == 'a':
                selected_option_name = a
                fa(selected_option, selected_option_name)
                return a
                
            elif selected_option == 'b':
                selected_option_name = b
                fb(selected_option, selected_option_name)
                return b
                
            elif selected_option == 'c':
                selected_option_name = c
                fc(selected_option, selected_option_name)
                return c
                
            else:
                selected_option_name = "Invalid Selection"
                self.view.display_selection(selected_option, selected_option_name)
                continue
    
    # returns the selected role to main.py
    def role_selection_handler(self):
        selected_option_name = self.menu_display_handler(fa=self.view.display_selection,
                                  fb=self.view.display_selection,
                                  fc=self.view.display_selection,
                                  a="Client",
                                  b="Librarian",
                                  c="Exit",
                                  screen=1)
        return selected_option_name
    
    # returns the selected option to main.py from authentication menu
    def user_authentication_handler(self):
        selected_option_name = self.menu_display_handler(fa=self.view.display_selection,
                                  fb=self.view.display_selection,
                                  fc=self.view.display_selection,
                                  a="Signup",
                                  b="Login",
                                  c="Exit",
                                  screen=2)
        return selected_option_name
    
    # handles the whole signup process
    def signup_handler(self, role):
        # declaring the variable
        selected_option = ''
        # keep continuing the loop if user has entered something other than a, b or c      
        while ((selected_option != 'Submit') or (selected_option != 'Cancel') or (selected_option != 'Exit')):
            # re-initializing for the case when need to re-run the loop 
            selected_option = ''
            # will hold the validity of each form input section
            validity_dict = {}
            # total form validity is false initially
            total_form_validity = False
            
            # showing the form and getting the user details for signup
            user_signup_dict = self.view.signup_form()
            
            # showing form submission options using "menu_display_handler" and getting the selected option as well
            selected_option = self.menu_display_handler(fa=self.view.display_selection,
                                  fb=self.view.display_selection,
                                  fc=self.view.display_selection,
                                  a="Submit",
                                  b="Cancel",
                                  c="Exit",
                                  screen=3)
            
            # if user has chosen other than a or b or c
            while True:
                if ((selected_option == 'Submit') or (selected_option == 'Cancel') or (selected_option == 'Exit')):
                    break
                else:
                    # again showing form submission options using "menu_display_handler" and getting the selected option as well
                    selected_option = self.menu_display_handler(fa=self.view.display_selection,
                        fb=self.view.display_selection,
                        fc=self.view.display_selection,
                        a="Submit",
                        b="Cancel",
                        c="Exit",
                        screen=3)
            
            # what to do if user has selected a or b or c
            # exit                 
            if (selected_option == 'Exit'):
                self.view.display_selection(selected_option, "Exit")
                self.exit_application_handler()
            # cancel
            # again bringing new form
            elif (selected_option == 'Cancel'):
                self.view.display_selection(selected_option, "Cancel")
                continue
            # submit
            elif (selected_option == 'Submit'):
                # validating name, email, password, phone number and putting individual status in the form of true/false in the "validity_dict" dictionary
                
                # name validator
                result = validator.name_validator(user_signup_dict["fname"],
                                                  user_signup_dict["lname"])
                # name validator result
                validity_dict["Name"] = result
                
                # email validator
                result = validator.email_validator(user_signup_dict["email"])
                # email validator result
                validity_dict["Email"] = result
                
                # password validator
                result = validator.password_validator(user_signup_dict["pass1"],user_signup_dict["pass2"])
                # password validator result
                validity_dict["Password"] = result
                
                # phone number valdator
                result = validator.ph_no_validator(user_signup_dict["ph"])
                # phone number valdator result
                validity_dict["Phone Number"] = result
                
                # checking whether any one of the validation result is false or not and based on that we are setting the overall validity of the form
                if (False in validity_dict.values()):
                    total_form_validity = False
                else:
                    total_form_validity = True
                
                # based on the overall validity we will either ask for form resubmission or forward the data to the model for inserting into the database
                if (total_form_validity == True):
                    break
                else:
                    self.view.signup_form_error(list
                                                (filter
                                                 (lambda item :
                                                      item[1] == False, validity_dict.items())))
        
        # signup method of Model inserts the data into database
        # it also calls another method from Model internally to create the user role as well
        # returns the request status and inserted user id
        return_data = self.model.signup(role, user_signup_dict)
        
        # if successfully created the user, then creating/inserting user role as well
        if (return_data[0] == "200"):
            self.view.signup_successful()
        elif (return_data[0] == "500"):
            self.view.signup_failed()
        
        # in the end showing the reduced authentication menu for login and exit
        # again the choice will be returned to the main.py
        while True:
            selected_option = self.view.auth_menu_after_signup()
            selected_option_name = lambda x : "Login" if x == 'a' else ("Exit" if x == 'b' else "Invalid Selection")
            
            self.view.display_selection(selected_option, selected_option_name(selected_option))
            
            if ((selected_option == 'a') or (selected_option == 'b')):
                if (selected_option == 'a'):
                    return "Login"
                elif (selected_option == 'b'):
                    return "Exit"
            else:
                continue
    
    def login_handler(self, role):
        print("Looooogggiinnnnn........", role)
                  
        
                
                    
            
            
                
                