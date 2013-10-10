from utilities.generalFunctions import *
from controller.switch import *


class EntitySwitch(Switch):
    """
    controller of entity
    """

    def __init__(self, gear):
        #parent constructor
        Switch.__init__(self, gear)
        #ASCII character representing the entity
        self.character = ''

    def callActionMove(self, destination):
        """
        display movement of the entity
        """
        #pass by default
        pass

    def callActionCanMoveTo(self, actionResult, destination = False):
        """
        display information about possibility of chosen move
        """
        pass