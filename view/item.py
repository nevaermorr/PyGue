from generalFunctions import *
from view.view import *


class ItemView(View):
    """
    display of item
    """

    def display(self):
        """
        display item on the screen
        """
        print('some item #' + str(self.model.id))