from app.models import Model
from app.views import View
from app import validator

class Controller:
    def __init__(self, view: View, model: Model):
        # model holds the object of Model class
        self.model = model
        # view holds the object of View class
        self.view = view
    
    def start_application_handler(self) -> None:
        self.view.greet_user()
    
    def exit_application_handler(self):
        self.view.exit_greet()
        exit()
    
    def menu_display_handler(self, fa, fb, fc, a, b, c, role=True, authentication=False):
        selected_option = ''
        selected_option_name = ''
        
        while ((selected_option != 'a') or (selected_option != 'b') or (selected_option != 'c')):
            if ((role == True) and (authentication == False)):
                selected_option = self.view.select_role_menu()
            elif ((authentication == True) and (role == False)):
                selected_option = self.view.authentication_menu()
            
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
    
    def role_selection_handler(self):
        selected_option_name = self.menu_display_handler(fa=self.view.display_selection,
                                  fb=self.view.display_selection,
                                  fc=self.view.display_selection,
                                  a="Client",
                                  b="Librarian",
                                  c="Exit")
        return selected_option_name
    
    def user_authentication_handler(self):
        selected_option_name = self.menu_display_handler(fa=self.view.display_selection,
                                  fb=self.view.display_selection,
                                  fc=self.view.display_selection,
                                  a="Signup",
                                  b="Login",
                                  c="Exit",
                                  role=False,
                                  authentication=True)
        return selected_option_name
        
    def signup_handler(self, role):
        selected_option = ''      
        while ((selected_option != 'a') or (selected_option != 'b') or (selected_option != 'c')):
            selected_option = ''
            validity_dict = {}
            total_form_validity = False
            
            user_signup_dict = self.view.signup_form()
            selected_option = self.view.form_submission_menu()
            
            while True:
                if ((selected_option == 'a') or (selected_option == 'b') or (selected_option == 'c')):
                    break
                else:
                    selected_option = self.view.form_submission_menu()
                    self.view.display_selection(selected_option, "Invalid Selection")
                                            
            if (selected_option == 'c'):
                self.view.display_selection(selected_option, "Exit")
                self.exit_application_handler()
            elif (selected_option == 'b'):
                self.view.display_selection(selected_option, "Cancel")
                continue
            elif (selected_option == 'a'):
                result = validator.name_validator(user_signup_dict["fname"],
                                                  user_signup_dict["lname"])
                validity_dict["Name"] = result
                
                result = validator.email_validator(user_signup_dict["email"])
                validity_dict["Email"] = result
                
                result = validator.password_validator(user_signup_dict["pass1"],user_signup_dict["pass2"])
                validity_dict["Password"] = result
                
                result = validator.ph_no_validator(user_signup_dict["ph"])
                validity_dict["Phone Number"] = result
                
                if (False in validity_dict.values()):
                    total_form_validity = False
                else:
                    total_form_validity = True
                
                if (total_form_validity == True):
                    print(total_form_validity)
                    break
                else:
                    self.view.signup_form_error(list
                                                (filter
                                                 (lambda item :
                                                      item[1] == False, validity_dict.items())))
                     
                    
                
                
                    
            
            
                
                