from pandas import DataFrame

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
    def display_selection(self, option, role):
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
    def signup_form_error(self, invalid_input_list: list) -> None:
        print("TLM> Invalid form input")
        print(
            f"TLM> Error in {list(i[0] for i in invalid_input_list)} input fields")
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

    # user already exist
    def user_already_exist(self, email):
        print(f"TLM> Email '{email}' already registered")

    # authentication menu display, selection and return
    def auth_menu_after_signup(self):
        print("\nPlease select an option:")
        print("(a) Login")
        print("(b) Exit")
        print("Enter a or b")

        selected_option = input("TLM> ")
        return selected_option

    # display login form and take input from the user for the form
    # returns the details entered by the user to the controller and controller take care of the logic from there
    def login_form(self):
        user_login_dict = {}

        print("\nPlease enter the following details to login:")
        user_login_dict["email"] = input("TLM> Email: ")
        user_login_dict["pass"] = input("TLM> Password: ")

        return user_login_dict

    # if user successfully logged in
    def login_greet(self, fname, lname):
        print("/////////////////////////////////////////////////////////////////")
        print(f"/////////////////////// Login Successful ////////////////////////")
        print("/////////////////////////////////////////////////////////////////")
        print(f"TLM> Welcome {fname} {lname} to the Login Dashboard")

    # correct email and password but wrong role selected
    def login_wrong_role(self, fname, lname):
        print(f"TLM> User {fname} {lname}, you have chosen a wrong role.")
        print(f"TML> The application will be closed for security reasons.")

    # wrong credentials and so login will fail
    def login_wrong_credential(self):
        print(f"TLM> You have entered invalid credentials.")
        print(f"TLM> Please try again...")

    # librarian menu
    def librarian_menu(self):
        menu_list = ["Exit",
                     "Issue a new book",
                     "Client book submission",
                     "Get all the books",
                     "Get rented books",
                     "Get all the rentable books",
                     "Add a book",
                     "Update a book",
                     "Delete a book",
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
        print("Enter a number between 0 to 10")

        selected_option_name = ""
        int_option = ""

        selected_option = input("TLM> ")

        try:
            int_option = int(selected_option)
        except Exception:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]

        if ((int_option >= 0) and int_option <= 10):
            selected_option_name = menu_list[int_option]
            return [selected_option, selected_option_name, menu_list]
        else:
            selected_option_name = "Invalid Input"
            return [selected_option, selected_option_name, menu_list]

    def view_all_books(self, data_list, column_names):
        data_frame = DataFrame(data_list, columns=column_names)
        print(data_frame.to_markdown(tablefmt="grid"))
    
    def get_book_id_user_id(self):
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
    
    # operation failure/successful in librarian handler
    def operation_message(self, message):
        print("/////////////////////////////////////////////////////////////////")
        print(f"{message}")
        print("/////////////////////////////////////////////////////////////////")
    
    # press any button to continue
    def press_button_continue(self):
        print("TLM> Please enter any button to continue...")
        input("TLM> ")
        
    # display fine details
    def display_fine_details(self, book_name, rented_on, rent_days, fine, user_name, user_email, due_fees, total_fees):
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
