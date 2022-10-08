from copy import deepcopy
import stat
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
        # returns the request status along with inserted user credentials/already exist or not
        return_data = self.model.signup(self.user_role, user_signup_dict)
        
        # if user already exist (status 401) we are giving choice to login or exit
        # no insert has happend in the database
        if (return_data[0] == "401"):
            self.view.user_already_exist(user_signup_dict["email"])
            self.view.signup_failed()
            user_signup_dict.clear()
            # showing the menu and and asking to choose
            while True:
                selected_option = self.view.auth_menu_after_signup()
                selected_option_name = lambda x : "Login" if x == 'a' else ("Exit" if x == 'b' else "Invalid Selection")
                
                self.view.display_selection(selected_option, selected_option_name(selected_option))
                
                # returning the choice login/exit to the main.py
                if ((selected_option == 'a') or (selected_option == 'b')):
                    if (selected_option == 'a'):
                        return "Login"
                    elif (selected_option == 'b'):
                        return "Exit"
                else:
                    continue
        
        # if user does not exist already
        # user details will be entered in the database and we will save the user id in the instance variable
        elif ((return_data[0] == "200") or (return_data[0] == "500")):
            # if successfully created the user, then creating/inserting user role as well
            if (return_data[0] == "200"):
                self.view.signup_successful()
                # setting app_user_id
                self.user_id = return_data[1][8]
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
    
    # will handle login and validation during login
    def login_handler(self):
        # getting credentials from user
        login_credential_dict = self.view.login_form()
        # validating user against the supplied credentials
        check_auth_role_response = self.model.check_user_existence_role(login_credential_dict["email"],
                                                                   login_credential_dict["pass"],
                                                                   self.user_role)
        
        # there could be three cases
        # 1 - got the user with corrent role
        if (check_auth_role_response[0] == "200"):
            # login_greet takes first name and last name
            self.view.login_greet(check_auth_role_response[1][0][1],
                                  check_auth_role_response[1][0][2])
            
            # setting user_id to current logged in user
            self.user__id = check_auth_role_response[1][0][0]
            
            # calling the librarian/client handler based on the role, selected initially at the first step in the application
            if (self.user_role == "Client"):
                self.client_handler()
            elif (self.user_role == "Librarian"):
                self.librarian_handler()
        
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

    # handle the logged in user when role is librarian
    def librarian_handler(self):
        while True:
            selected_menu = self.view.librarian_menu()
            # 0 is option, 1 is option name, 2 is list of valid options
            self.view.display_selection(selected_menu[0], selected_menu[1])
            # if selected option is in the list (means, not an Invalid Option)
            if (selected_menu[1] in selected_menu[2]):
                break
            else:
                continue
            
        #=================================================================================
        # 0 - Exit
        #=================================================================================
        if (selected_menu[1] == "Exit"):
            self.exit_application_handler()
        #=================================================================================
        # 1 - Issue a book
        #=================================================================================
        elif (selected_menu[1] == "Issue a new book"):
            ids = self.view.get_book_id_user_id()
            
            if(None not in ids):
                status = self.model.book_issue(app_user_id=self.user_id,
                                                    user_id=ids[1],
                                                    book_id=ids[0])
                # if status 200
                if (status[0] == "200"):
                    self.view.operation_message("Book issued Successfully")           
                elif (status[0] == "500"):
                    self.view.operation_message("Failed to issue the book")
            
            self.view.press_button_continue()              
        #=================================================================================
        # 2 - Return a book
        #=================================================================================
        elif (selected_menu[1] == "Client book submission"):
            ids = self.view.get_book_id_user_id()
            
            if(None not in ids):
                status = self.model.book_return(app_user_id=self.user_id,
                                                    user_id=ids[1],
                                                    book_id=ids[0])
                # if status 200
                if (status[0] == "200"):
                    self.view.operation_message("Book returned Successfully")
                    self.view.display_fine_details(book_name=status[1],
                                                   rented_on=status[2],
                                                   rent_days=status[3],
                                                   fine= status[4],
                                                   user_name=status[5],
                                                   user_email=status[6],         
                                                   due_fees=status[7],         
                                                   total_fees=status[8])         
                elif (status[0] == "500"):
                    self.view.operation_message("Failed to return the book")
            
            self.view.press_button_continue()              
        
        #=================================================================================
        # 3 - Fees Submission
        #=================================================================================
        elif (selected_menu[1] == "Fees Submission"):
            ids = self.view.get_book_id_user_id(book_id=False, fees=True)
            
            status = self.model.submit_fees(app_user_id=self.user_id,
                                            user_id=ids[0],
                                            fees=ids[1])
            
            if (status[0] == "200"):
                self.view.display_fees_submission(user_name=status[1],
                                                  user_email=status[2],
                                                  due_fees=status[3],
                                                  submitted_fees=ids[1],
                                                  remaining_fees=status[4])
            elif (status[0] == "500"):
                 self.view.operation_message("Failed to submit the fees")
        
            self.view.press_button_continue()
                                       
        #=================================================================================
        # 4 - Get all the books
        #=================================================================================
        elif (selected_menu[1] == "Get all the books"):
            column_names_string = ""
            # asking from Model
            column_names = ["book_id",
                            "user_id",
                            "book_name",
                            "book_author",
                            "publication_company",
                            "is_rented"]
            
            for item in column_names:
                column_names_string += f"{item},"
            
            column_names_string = column_names_string[:len(column_names_string)-1]
            
            # model method call    
            all_books = self.model.get_all_books(column_names=column_names_string)
            
            # if status 200
            if (all_books[0] == "200"):
                self.view.view_all_books(all_books[1],column_names)
            else:
                self.view.operation_message("Failed to fetch all books list")
            
            self.view.press_button_continue()  
        #=================================================================================
        # 5 - get rented books
        #=================================================================================
        elif (selected_menu[1] == "Get rented books"):
            column_names_string = ""
            # asking from Model
            column_names = ["book_id",
                            "user_id",
                            "book_name",
                            "book_author",
                            "publication_company",
                            "is_rented",
                            "rented_on"]
            
            for item in column_names:
                column_names_string += f"{item},"
            
            column_names_string = column_names_string[:len(column_names_string)-1]
            
            # model method call
            all_books = self.model.get_all_books(column_names=column_names_string, where_clause="is_rented=1")
            
            # if status 200
            if (all_books[0] == "200"):
                self.view.view_all_books(all_books[1],column_names)
            else:
                self.view.operation_message("Failed to fetch rented books list")
            
            self.view.press_button_continue()  
        #=================================================================================
        # 6 - get rentable books
        #=================================================================================
        elif (selected_menu[1] == "Get all the rentable books"):
            column_names_string = ""
            # asking from Model
            column_names = ["book_id",
                            "user_id",
                            "book_name",
                            "book_author",
                            "publication_company",
                            "is_rented"]
            
            for item in column_names:
                column_names_string += f"{item},"
            
            column_names_string = column_names_string[:len(column_names_string)-1]
            
            # model method call
            all_books = self.model.get_all_books(column_names=column_names_string, where_clause="is_rented=0")
            
            # if status 200
            if (all_books[0] == "200"):
                self.view.view_all_books(all_books[1],column_names)
            else:
                self.view.operation_message("Failed to fetch rentable books list")
                
            self.view.press_button_continue()
        
        #=================================================================================
        # 7 - upload a new book
        #================================================================================= 
        elif (selected_menu[1] == "Upload a book"):
            book_details_list = self.view.get_book_details(app_user_id=self.user_id)
            status = self.model.upload_book(book_details_list)
            
            if (status[0] == "200"):
                self.view.display_created_book(status[1])
            elif (status[0] == "500"):
                self.view.operation_message("Failed to upload the new book")
            
            self.view.press_button_continue()
        
        #=================================================================================
        # 8 - update a book
        #================================================================================= 
        elif (selected_menu[1] == "Update a book"):
            book_details_list = self.view.get_book_details(app_user_id=self.user_id,
                                                           create=False,
                                                           delete=False,
                                                           edit=True)
            status = self.model.edit_book(book_details_list)
            
            if (status == "200"):
                self.view.operation_message("Updated the book Successfully")
            elif (status == "500"):
                self.view.operation_message("Failed to update the book")
            
            self.view.press_button_continue()
        
        #=================================================================================
        # 9 - delete a book
        #================================================================================= 
        elif (selected_menu[1] == "Delete a book"):
            book_delete = self.view.get_book_details(app_user_id=self.user_id,
                                                           create=False,
                                                           delete=True)
            delete_status = self.model.delete_book(app_user_id=book_delete[1],
                                            book_id=book_delete[0])
            if (delete_status == "200"):
                self.view.operation_message("Deleted the book Successfully")
            elif (delete_status == "500"):
                self.view.operation_message("Failed to delete the book")
            
            self.view.press_button_continue()        

        #=================================================================================
        # 10 - get user details with role
        #=================================================================================
        elif (selected_menu[1] == "Get user details"):
            user_role_status = self.model.get_user_with_role()
            column_names = ["user_id",
                            "first_name",
                            "last_name",
                            "role_type_name",
                            "email",
                            "password",
                            "phone_number",
                            "fees"]
            
            if (user_role_status[0] == "200"):
                self.view.view_all_users(user_role_status[1][0], column_names)
            elif (user_role_status[0] == "500"):
                self.view.operation_message("Failed to fetch the users")
            
            self.view.press_button_continue()
                    
        #=================================================================================
        # 11 - update an user
        #=================================================================================
        elif (selected_menu[1] == "Update an user"):
            user_details = self.view.get_edit_user_details(app_user_id=self.user_id)
            user_update_status = self.model.edit_user(edit_user_details=user_details)
            
            if (user_update_status == "200"):
                self.view.operation_message("User updated successfully")
            elif (user_update_status == "500"):
                self.view.operation_message("Failed to update the user details")
            
            self.view.press_button_continue()        
                                
        #=================================================================================
        # 12 - delete an user
        #=================================================================================
        elif (selected_menu[1] == "Delete an user"):
            user_details = self.view.get_edit_user_details(app_user_id=self.user_id, edit=False, delete=True)
            user_delete_status = self.model.delete_user(edit_user_details=user_details)
            
            if (user_delete_status == "200"):
                self.view.operation_message("User deleted successfully")
            elif (user_delete_status == "500"):
                self.view.operation_message("Failed to delete the user")
            
            self.view.press_button_continue()        
                   
        # calling self again (recursion)
        self.librarian_handler()

    def client_handler(self):
        while True:
            selected_menu = self.view.client_menu()
            # 0 is option, 1 is option name, 2 is list of valid options
            self.view.display_selection(selected_menu[0], selected_menu[1])
            # if selected option is in the list (means, not an Invalid Option)
            if (selected_menu[1] in selected_menu[2]):
                break
            else:
                continue
        
        #=================================================================================
        # 0 - Exit
        #=================================================================================
        if (selected_menu[1] == "Exit"):
            self.exit_application_handler()
        #=================================================================================
        # 1 - Get rentable books
        #=================================================================================
         
        elif (selected_menu[1] == "Get rentable books"):
            column_names_string = ""
            # asking from Model
            column_names = ["book_id",
                            "book_name",
                            "book_author",
                            "publication_company"]
            
            for item in column_names:
                column_names_string += f"{item},"
            
            column_names_string = column_names_string[:len(column_names_string)-1]
            
            # model method call
            all_books = self.model.get_all_books(column_names=column_names_string, where_clause="is_rented=0")
            
            # if status 200
            if (all_books[0] == "200"):
                self.view.view_all_books(all_books[1],column_names)
            else:
                self.view.operation_message("Failed to fetch rentable books list")
                
            self.view.press_button_continue()
        
        #=================================================================================
        # 2 - View book details
        #=================================================================================
        
        elif (selected_menu[1] == "View book details"):
            column_names_string = ""
            # asking from Model
            column_names = ["book_id",
                            "book_name",
                            "book_desc"]
            
            for item in column_names:
                column_names_string += f"{item},"
            
            column_names_string = column_names_string[:len(column_names_string)-1]
            
            # model method call
            all_books = self.model.get_all_books(column_names=column_names_string, where_clause="is_rented=0")
            
            # if status 200
            if (all_books[0] == "200"):
                self.view.view_all_books(all_books[1],column_names)
            else:
                self.view.operation_message("Failed to fetch the book details")
                
            self.view.press_button_continue()
        
        #=================================================================================
        # 3 - View my profile
        #=================================================================================
        
        elif (selected_menu[1] == "Get my profile"):
            user_role_status = self.model.get_single_user_with_role(user_id=self.user_id)
            column_names = ["user_id",
                            "first_name",
                            "last_name",
                            "role_type_name",
                            "email",
                            "password",
                            "phone_number",
                            "fees"]
            
            if (user_role_status[0] == "200"):
                self.view.view_all_users(user_role_status[1], column_names)
            elif (user_role_status[0] == "500"):
                self.view.operation_message("Failed to fetch the profile details")
            
            self.view.press_button_continue()
            
        #=================================================================================
        # 4 - Edit my profile
        #=================================================================================
        elif (selected_menu[1] == "Update my profile"):
            user_details = self.view.get_edit_user_details(app_user_id=self.user_id, own=True)
            user_update_status = self.model.edit_user(edit_user_details=user_details)
            
            if (user_update_status == "200"):
                self.view.operation_message("Profile updated successfully")
            elif (user_update_status == "500"):
                self.view.operation_message("Failed to update the profile")
            
            self.view.press_button_continue()
            
        # calling self again (recursion)
        self.client_handler()            

                
                