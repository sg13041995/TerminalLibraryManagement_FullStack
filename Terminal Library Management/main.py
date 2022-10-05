# import app module/folder and all it's content/files
from app import *

# using csql module to parse the mysql credential
# then using the credentials to create a connection with the database
# also saving the connection and cursor object
credentials_dict = csql.credential_parser()
connection_object, cursor_object = csql.connect_db(credentials_dict)

# holds the user selections from role and authentication menu
role_selection = ""
auth_selection = ""
# this id is requied during user signup as the "app_user_id" in the database because, the user's id is getting registered and during this process we need to enter a app_user_id which cannot be equal to the newly created user
super_admin_id = 1

# at the start of the application controller is instantiating a controller object which in turn takes the model and view objects as argumets
# View() and Model() is creating the objects of the respective classes on the fly
# when creating object of Model class we are also passing the connection and cursor object to the Model object
controller = controllers.Controller(views.View(), models.Model(connection_object, 
                                                               cursor_object, 
                                                               super_admin_id))

# "start_application_handler" method is the entry point of the application
# greetings to the user
controller.start_application_handler()

# "role_selection_handler" method displays the role selection menu and returns the selected role
# role_selection -> Client/Librarian/Exit
role_selection = controller.role_selection_handler()

# if "Exit" has been selected then we will call "exit_application_handler" to quit the application
if role_selection == "Exit":
    controller.exit_application_handler()

# if user has chosen "Client" or "Librarian" from role menu then we will display authentication menu by calling "user_authentication_handler" method
elif ((role_selection == "Client") or (role_selection == "Librarian")):
    # auth_selection -> Signup/Login/Exit
    auth_selection = controller.user_authentication_handler()
# again at this point, if the user wants to exit then we will again call "exit_application_handler" to quit the application
if auth_selection == "Exit":
    controller.exit_application_handler()
# otherwise we will handle the selected option
# starting with Signup functionality
elif (auth_selection == "Signup"):
    # next_selected_option -> Login/Exit
    # user__role is a setter function
    controller.user__role = role_selection
    next_selected_option = controller.signup_handler()
    # if "Exit" has been selected then we will call "exit_application_handler" to quit the application
    if (next_selected_option == "Exit"):
        controller.exit_application_handler()
    elif (next_selected_option == "Login"):
        controller.login_handler()
# handling Login functionality
elif (auth_selection == "Login"):
    # user__role is a setter function
    controller.user__role = role_selection
    controller.login_handler()