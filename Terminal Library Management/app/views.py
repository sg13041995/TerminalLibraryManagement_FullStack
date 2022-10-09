# pandas will help to display records in a readable manner
from pandas import DataFrame

# class definition
class View:
    # constructor
    def __init__(self) -> None:
        pass

    # initial greet on start of the applicaion
    def greet_user(self) -> None:
        print("//////////////////////////////////////////////////////////////")
        print("///////// Welcome to the Terminal Library Management /////////")
        print("//////////////////////////////////////////////////////////////")

    # exit greet when user quits the application
    def exit_greet(self) -> None:
        print("TLM> Quiting the application...")
        print("//////////////////////////////////////////////////////////////")
        print("//////////// Thank you for using the application /////////////")
        print("//////////////////////////////////////////////////////////////")

    # role menu display, selection and return
    def select_role_menu(self) -> str:
        print("\nPlease select a role:")
        print("(a) Client")
        print("(b) Librarian")
        print("(c) Exit")
        print("Enter a or b or c")

        selected_option = input("TLM> ")
        return selected_option

    # display the entered value and corresponding option if any
    def display_selection(self, option : str, role : str) -> None:
        print(f"TLM> You have selected '{option}' => '{role}'")

    # authentication menu display, selection and return
    def authentication_menu(self) -> str:
        print("\nPlease select an option:")
        print("(a) Signup")
        print("(b) Login")
        print("(c) Exit")
        print("Enter a or b or c")

        selected_option = input("TLM> ")
        return selected_option

    # display signup form and take input from the user for the form
    def signup_form(self) -> dict:
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
    def form_submission_menu(self) -> str:
        print("\nPlease select an option:")
        print("(a) Submit")
        print("(b) Cancel")
        print("(c) Exit")
        print("Enter a or b or c")

        selected_option = input("TLM> ")
        return selected_option

    # if there is some error in the user input for the form then display the input field where user has made the mistake or form validity failed
    def signup_form_error(self, invalid_input_list: list) -> None:
        print("TLM> Invalid form input")
        print(
            f"TLM> Error in {list(i[0] for i in invalid_input_list)} input fields")
        print("Please try again...")

    # message on successful signup
    def signup_successful(self) -> None:
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////// Signup Successful //////////////////////")
        print("//////////////////////////////////////////////////////////////")

    # message on signup failure
    def signup_failed(self) -> None:
        print("//////////////////////////////////////////////////////////////")
        print("//////////////////////// Signup Failed ///////////////////////")
        print("//////////////////////////////////////////////////////////////")

    # user already exist
    def user_already_exist(self, email : str) -> None:
        print(f"TLM> Email '{email}' already registered")

    # authentication menu display, selection and return
    def auth_menu_after_signup(self) -> str:
        print("\nPlease select an option:")
        print("(a) Login")
        print("(b) Exit")
        print("Enter a or b")

        selected_option = input("TLM> ")
        return selected_option

    # display login form and take input from the user for the form
    # returns the details entered by the user to the controller and controller take care of the logic from there
    def login_form(self) -> dict:
        user_login_dict = {}

        print("\nPlease enter the following details to login:")
        user_login_dict["email"] = input("TLM> Email: ")
        user_login_dict["pass"] = input("TLM> Password: ")

        return user_login_dict

    # if user successfully logged in
    def login_greet(self, fname : str, lname : str) -> None:
        print("/////////////////////////////////////////////////////////////////")
        print(f"/////////////////////// Login Successful ////////////////////////")
        print("/////////////////////////////////////////////////////////////////")
        print(f"TLM> Welcome {fname} {lname} to the Login Dashboard")

    # correct email and password but wrong role selected
    def login_wrong_role(self, fname : str, lname : str) -> None:
        print(f"TLM> User {fname} {lname}, you have chosen a wrong role.")
        print(f"TML> The application will be closed for security reasons.")

    # wrong credentials and so login will fail
    def login_wrong_credential(self) -> None:
        print(f"TLM> You have entered invalid credentials.")
        print(f"TLM> Please try again...")

    # librarian menu
    def librarian_menu(self) -> None:
        menu_list = ["Exit",
                     "Issue a new book",
                     "Client book submission",
                     "Fees Submission",
                     "Get all the books",
                     "Get rented books",
                     "Get all the rentable books",
                     "Upload a book",
                     "Update a book",
                     "Delete a book",
                     "Get user details",
                     "Update an user",
                     "Delete an user"]
        print("\nPlease select an option:")
        print(f"(0) {menu_list[0]}")
        print(f"(1) {menu_list[1]}")
        print(f"(2) {menu_list[2]}")
        print(f"(3) {menu_list[3]}")
        print(f"(4) {menu_list[4]}")
        print(f"(5) {menu_list[5]}")
        print(f"(6) {menu_list[6]}")
        print(f"(7) {menu_list[7]}")
        print(f"(8) {menu_list[8]}")
        print(f"(9) {menu_list[9]}")
        print(f"(10) {menu_list[10]}")
        print(f"(11) {menu_list[11]}")
        print(f"(12) {menu_list[12]}")
        print("Enter a number between 0 to 12")

        selected_option_name = ""
        int_option = ""

        selected_option = input("TLM> ")

        try:
            int_option = int(selected_option)
        except Exception:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]

        if ((int_option >= 0) and int_option <= 12):
            selected_option_name = menu_list[int_option]
            return [selected_option, selected_option_name, menu_list]
        else:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]

    # view all the available books list
    def view_all_books(self, data_list : list, column_names : list) -> None:
        data_frame = DataFrame(data_list, columns=column_names)
        print(data_frame.to_markdown(tablefmt="grid"))
    
    # get book id and user id for controller
    def get_book_id_user_id(self, book_id : bool=True, user_id : bool=True, fees : bool=False) -> list:
        if((user_id == True) and (book_id == True)):
            print("TLM> Please enter the book id:")
            book_id = input("TLM> ")
            print("TLM> Please enter the user id:")
            user_id = input("TLM> ")
            try:
                book_id = abs(int(book_id))
                user_id = abs(int(user_id))
                
                return [book_id, user_id]
            except Exception:
                return [None, None]
            
        elif((user_id == False) and (book_id == True)):
            print("TLM> Please enter the book id:")
            book_id = input("TLM> ")
            try:
                book_id = abs(int(book_id))
                
                return book_id
            except Exception:
                return None
            
        elif((user_id == True) and (book_id == False)):
            print("TLM> Please enter the user id:")
            user_id = input("TLM> ")
            submit_fees = "0"
            if (fees == True):
                print("TLM> Please enter the fees submission amount:")
                submit_fees = input("TLM> ")
            try:
                user_id = abs(int(user_id))
                submit_fees = abs(int(submit_fees))
                return [user_id, submit_fees]
            except Exception:
                return [None, None]
    
    
    
    # operation failure/successful in librarian handler
    def operation_message(self, message : str) -> None:
        print("/////////////////////////////////////////////////////////////////")
        print(f"{message}")
        print("/////////////////////////////////////////////////////////////////")
    
    # press any button to continue
    def press_button_continue(self) -> None:
        print("TLM> Please enter any button to continue...")
        input("TLM> ")
        
    # display fine details
    def display_fine_details(self, book_name, rented_on, rent_days, fine, user_name, user_email, due_fees, total_fees) -> None:
        print("/////////////////////////////////////////////////////////////////")
        print(f"User Name: {user_name}")
        print(f"User Email: {user_email}")
        print(f"Book Name: {book_name}")
        print(f"Book Rented on: {rented_on}")
        print(f"Book Rented for: {rent_days} day(s)")
        print(f"Fine: {fine} Rupees")
        print(f"Due Fees: {due_fees} Rupees")
        print(f"Total Fees: {total_fees} Rupees")
        print("/////////////////////////////////////////////////////////////////")
    
    # display fees submission
    def display_fees_submission(self, user_name, user_email, due_fees, submitted_fees, remaining_fees):
        print("/////////////////////////////////////////////////////////////////")
        print(f"User Name: {user_name}")
        print(f"User Email: {user_email}")
        print(f"Previous Due Fees: {due_fees} Rupees")
        print(f"Submitted Fees: {submitted_fees} Rupees")
        print(f"Remaining Fees: {remaining_fees} Rupees")
        print("/////////////////////////////////////////////////////////////////")

    # collect book details during create, edit, delete
    def get_book_details(self, app_user_id, create=True, delete=False, edit=False):
        edit_book_id=None
        if (delete == True):
            print("TLM> Please enter the book id:")
            book_id = input("TLM> ")
            if(book_id == ""):
                edit_book_id = None
                app_user_id = None
                return [edit_book_id, app_user_id]
            else:
                edit_book_id = book_id
                return [edit_book_id, app_user_id]
        
        elif (edit == True):
            book_details_list = [0,
                                app_user_id,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None]
            
            print("TLM> Please enter the book id:")
            book_id = input("TLM> ")
            if(book_id == ""):
                edit_book_id = None
                book_details_list[2] = edit_book_id
            else:
                edit_book_id = book_id
                book_details_list[2] = edit_book_id
            
            print("TLM> Please enter the book name:")
            book_name = input("TLM> ")
            if(book_name == ""):
                book_name = None
                book_details_list[4] = book_name
            else:
                book_details_list[4] = book_name
                                
            print("TLM> Please enter the book description:")
            book_desc = input("TLM> ")
            if(book_desc == ""):
                book_desc = None
                book_details_list[5] = book_desc
            else:
                book_details_list[5] = book_desc
            
            print("TLM> Please enter the book author:")
            book_author = input("TLM> ")
            if(book_author == ""):
                book_author = None
                book_details_list[6] = book_author
            else:
                book_details_list[6] = book_author
            
            print("TLM> Please enter the book publication company:")
            book_publication_company = input("TLM> ")
            if(book_publication_company == ""):
                book_publication_company = None
                book_details_list[7] = book_publication_company
            else:
                book_details_list[7] = book_publication_company
            
            print("TLM> Please enter the book ISBN:")
            book_isbn = input("TLM> ")
            if(book_isbn == ""):
                book_isbn = None
                book_details_list[8] = book_isbn
            else:
                book_details_list[8] = book_isbn
            
            return book_details_list
        
        else:
            book_details_list = [0,
                                app_user_id,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                0]
            
            print("TLM> Please enter the book name:")
            book_name = input("TLM> ")
            if(book_name == ""):
                pass
            elif(book_name == "None"):
                book_details_list[2] = None
            else:
                book_details_list[2] = book_name
                                
            print("TLM> Please enter the book description:")
            book_desc = input("TLM> ")
            if(book_desc == ""):
                pass
            elif(book_desc == "None"):
                book_details_list[3] = None
            else:
                book_details_list[3] = book_desc
            
            print("TLM> Please enter the book author:")
            book_author = input("TLM> ")
            if(book_author == ""):
                pass
            elif(book_author == "None"):
                book_details_list[4] = None
            else:
                book_details_list[4] = book_author
            
            print("TLM> Please enter the book publication company:")
            book_publication_company = input("TLM> ")
            if(book_publication_company == ""):
                pass
            elif(book_publication_company == "None"):
                book_details_list[5] = None
            else:
                book_details_list[5] = book_publication_company
            
            print("TLM> Please enter the book ISBN:")
            book_isbn = input("TLM> ")
            if(book_isbn == ""):
                pass
            elif(book_isbn == "None"):
                book_details_list[6] = None
            else:
                book_details_list[6] = book_isbn
            
            return book_details_list
    
    def display_created_book(self,book_details_tuple):
        print("/////////////////////////////////////////////////////////////////")
        print(f"Book Name: {book_details_tuple[2]}")
        print(f"Book Description: {book_details_tuple[3]}")
        print(f"Book Author: {book_details_tuple[4]}")
        print(f"Publication Company: {book_details_tuple[5]}")
        print(f"ISBN: {book_details_tuple[6]}")
        print("/////////////////////////////////////////////////////////////////")

    def view_all_users(self, data_list, column_names):
        data_frame = DataFrame(data_list, columns=column_names)
        print(data_frame.to_markdown(tablefmt="grid"))
        
    def get_edit_user_details(self, app_user_id, edit=True, delete=False, own=False):
        edit_user_details_list = [0,
                                 app_user_id,
                                 None, 
                                 None,
                                 None,
                                 None,
                                 None,
                                 None,
                                 None,
                                 None]
        
        if (delete == True):
            print("TLM> Please enter the user id:")
            user_id = input("TLM> ")
            if(user_id == ""):
                user_id = "###"
                edit_user_details_list[2] = user_id
            else:
                edit_user_details_list[2] = user_id
            
            edit_user_details_list[9] = 0
            
            return edit_user_details_list             
        
        if (edit ==True):
            if(own == True):
                edit_user_details_list[2] = app_user_id
            elif(own == False):
                print("TLM> Please enter the user id:")
                user_id = input("TLM> ")
                if(user_id == ""):
                    user_id = "###"
                    edit_user_details_list[2] = user_id
                else:
                    edit_user_details_list[2] = user_id
            
            print("TLM> Please enter the first name:")
            f_name = input("TLM> ")
            if(f_name == ""):
                f_name = None
                edit_user_details_list[3] = f_name
            else:
                edit_user_details_list[3] = f_name
                                
            print("TLM> Please enter the last name:")
            l_name = input("TLM> ")
            if(l_name == ""):
                l_name = None
                edit_user_details_list[4] = l_name
            else:
                edit_user_details_list[4] = l_name

            if(own == True):
                edit_user_details_list[5] = None
            elif(own == False):
                print("TLM> Please enter the email:")
                user_email = input("TLM> ")
                if(user_email == ""):
                    user_email = None
                    edit_user_details_list[5] = user_email
                else:
                    edit_user_details_list[5] = user_email
            
            print("TLM> Please enter the password:")
            user_password = input("TLM> ")
            if(user_password == ""):
                user_password = None
                edit_user_details_list[6] = user_password
            else:
                edit_user_details_list[6] = user_password
            
            if(own == True):
                edit_user_details_list[7] = None
            elif(own == False):
                print("TLM> Please enter the phone number:")
                phone_number = input("TLM> ")
                if(phone_number == ""):
                    phone_number = None
                    edit_user_details_list[7] = phone_number
                else:
                    edit_user_details_list[7] = phone_number
            
            if(own == True):
                edit_user_details_list[8] = None
            elif(own == False):
                print("TLM> Please enter the fees:")
                user_fees = input("TLM> ")
                if(user_fees == ""):
                    user_fees = None
                    edit_user_details_list[8] = user_fees
                else:
                    edit_user_details_list[8] = user_fees
            
            return edit_user_details_list
        
    # client menu
    def client_menu(self):
        menu_list = ["Exit",
                     "Get rentable books",
                     "View book details",
                     "Get my profile",
                     "Update my profile"]
        print("\nPlease select an option:")
        print(f"(0) {menu_list[0]}")
        print(f"(1) {menu_list[1]}")
        print(f"(2) {menu_list[2]}")
        print(f"(3) {menu_list[3]}")
        print(f"(4) {menu_list[4]}")
        print("Enter a number between 0 to 4")

        selected_option_name = ""
        int_option = ""

        selected_option = input("TLM> ")

        try:
            int_option = int(selected_option)
        except Exception:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]

        if ((int_option >= 0) and int_option <= 4):
            selected_option_name = menu_list[int_option]
            return [selected_option, selected_option_name, menu_list]
        else:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]