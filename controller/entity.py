from utilities.generalFunctions import *
from controller.switch import *


class EntitySwitch(Switch):
    """
    controller of entity
    """

    def __init__(self, gear):
        # parent constructor
        Switch.__init__(self, gear)
        # ASCII character representing the entity
        self.character = ''

    def call_action_move(self, destination):
        """
        display movement of the entity
        """
        # pass by default
        pass

    def call_action_can_move_to(self, action_result, destination=False):
        """
        display information about possibility of chosen move
        """
        pass