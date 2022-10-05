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
        self.user_id = None
        self.user_role = None
    
    @property
    def user__role(self):
        return self.user_role
    
    @user__role.setter
    def user__role(self, user_role):
        self.user_role = user_role
    
    @property
    def user__id(self):
        return self.user_id
    
    @user__id.setter
    def user__id(self, user_id):
        self.user_id = user_id
    
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
    def signup_handler(self):
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
        
        # signup method of Model fist check the user existence and then inserts the data into database
        # it also calls another method from Model internally to create/register the user role as well
        # self.user_role is an instance variable
        # returns the request status and inserted user credentials
        return_data = self.model.signup(self.user_role, user_signup_dict)
        print(return_data)
        
        if (return_data[0] == "401"):
            self.view.user_already_exist(user_signup_dict["email"])
            self.view.signup_failed()
            user_signup_dict.clear()
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
            
        elif ((return_data[0] == "200") or (return_data[0] == "500")):
            # setting app_user_id
            self.user_id = return_data[1][8]
            
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
    
    def login_handler(self):
        login_credential_dict = self.view.login_form()
        check_auth_role_response = self.model.check_user_existence_role(login_credential_dict["email"],
                                                                   login_credential_dict["pass"],
                                                                   self.user_role)
        
        # there could be three cases
        # 1 - got the user with corrent role
        if (check_auth_role_response[0] == "200"):
            self.view.login_greet(check_auth_role_response[1][0][1],
                                  check_auth_role_response[1][0][2])
        
        # 2 - got the user but with incorrect role
        # application will exit for security reasons
        elif(check_auth_role_response[0] == "404" and check_auth_role_response[2] == False):
            self.view.login_wrong_role(check_auth_role_response[1][0][1],
                                  check_auth_role_response[1][0][2])
            self.exit_application_handler()
        
        # 3 - didn't get the user because of wrong email-password combination
        # we will again call the login_handler(recursion)
        elif(check_auth_role_response[0] == "404" and check_auth_role_response[2] == None):
            self.view.login_wrong_credential()
            self.login_handler()
        
    def client_handler(self):
        print("client_handler")

    def librarian_handler(self):
        print("librarian_handler")
                  
        
                
                    
            
            
                
                