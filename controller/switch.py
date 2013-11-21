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
        # place for reference to panel - object responsible for displaying gear on screen
        self.panel = None

    def get_panel(self):
        """
        accessor for panel
        """
        return self.panel

    def display(self):
        """
        present element on the reel
        """
        # to be implemented by inheriting switches
        pass