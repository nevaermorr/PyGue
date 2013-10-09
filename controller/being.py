from controller.entity import *


class BeingController(EntityController):
    """
    display of being
    """

    def __init__(self, model):
        #parent constructor
        EntityController.__init__(self, model)

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

