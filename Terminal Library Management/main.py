# import app and its content
from app import *

role_selection = ""
auth_selection = ""

# at the start of the application controller is instantiating a controller object which in turn takes the model and view objects as argumets
# View() and Model() is creating the objects of the respective classes on the fly
controller = controllers.Controller(views.View(), models.Model())

# "start_application_handler" method is the entry point of the application
controller.start_application_handler()

# "role_selection_handler" method displays the role selection menu and returns the selected role
role_selection = controller.role_selection_handler()

# if "Exit" has been selected then we will call "exit_application_handler" to quit the application
if role_selection == "Exit":
    controller.exit_application_handler()
# if use has chosen "Client" or "Librarian" then we will display authentication menu by calling "user_authentication_handler" method
elif ((role_selection == "Client") or (role_selection == "Librarian")):
    auth_selection = controller.user_authentication_handler()

# again at this point, if the user wants to exit then we will again call "exit_application_handler" to quit the application
if auth_selection == "Exit":
    controller.exit_application_handler()
elif (auth_selection == "Signup"):
    controller.signup_handler(auth_selection)