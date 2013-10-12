from utilities.generalFunctions import *
from controller.entity import *


class BeingSwitch(EntitySwitch):
    """
    controller of being
    """

    def __init__(self, gear):
        # parent constructor
        EntitySwitch.__init__(self, gear)

    def choose_action(self):
        """
        decide what to do
        """
        # pass by default
        return ['wait']

    def call_action_collect(self, action_result, collected_items_=[]):
        """
        display information that the being collected some items
        """
        pass

    def call_action_drop(self, action_result, dropped_items_=[]):
        """
        display information that the being collected some items
        """
        pass

