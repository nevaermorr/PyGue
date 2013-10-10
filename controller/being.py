from utilities.generalFunctions import *
from controller.entity import *


class BeingSwitch(EntitySwitch):
    """
    controller of being
    """

    def __init__(self, gear):
        #parent constructor
        EntitySwitch.__init__(self, gear)

    def chooseAction(self):
        """
        decide what to do
        """
        #pass by default
        return ['wait']

    def callActionCollect(self, actionResult, collectedItems_=[]):
        """
        display information that the being collected some items
        """
        pass

    def callActionDrop(self, actionResult, droppedItems_=[]):
        """
        display information that the being collected some items
        """
        pass

