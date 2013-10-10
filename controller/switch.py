from utilities.generalFunctions import *

class Switch:
    """
    base class for all parts of controller
    """

    def __init__(self, gear):
        """
        :param gear: object to be controlled by this particular switch
        """
        self.gear = gear
        pass

    def display(self):
        """
        present element on the screen
        """
        #to be implemented by inheriting views
        pass