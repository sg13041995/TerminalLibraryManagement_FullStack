# We can use either of the following method to export the module files

# On the first method we need to do => 'import app' from main.py
# all content like Controller(), Model(), View() of controllers.py and so on will be under the name 'app'. 
# To use them we need to write => app.Controller() and so on.

# ===========================================
# code
# ===========================================
# from calculator.controllers import *
# from calculator.views import *
# from calculator.models import *
# ===========================================


# In the second method we can do the following => 'from calculator import *' from main.py
# This time all the content like Controller(), Model(), View() of controllers.py and so on will be under their own respective file name. 
# To use them we can write => controllers.Controller(), models.Model() and so on.

# ==============================================
# code (__all__ is a dunder variable actually)
# ==============================================
__all__ = ["controllers", "views", "models", "validator"]
# ==============================================