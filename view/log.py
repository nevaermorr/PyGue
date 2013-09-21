from generalFunctions import *
from view.view import *


class LogView(View):
    """
    display of logged information
    """

    def __init__(self, model):
        View.__init__(self, model)
        #start with empty information
        self.information = ''

    def display(self):
        """
        put the log on screen
        """
        print(self.information)