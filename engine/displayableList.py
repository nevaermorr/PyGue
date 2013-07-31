from engine.generalFunctions import *


class DisplayableList:
    """
    a list with methods for printing and selecting items from screen
    """

    def __init__(self):
        #base of this class - list of elements
        self.elements_ = []

    def displayElements(self):
        """
        display
        """