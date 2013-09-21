from generalFunctions import *


class View:
    """
    base class for all parts of view
    """

    def __init__(self, model):
        """
        :param model: object to be displayed by this particular view
        """
        self.model = model
        pass

    def display(self):
        """
        present element on the screen
        """
        #to be implemented by inheriting views
        pass