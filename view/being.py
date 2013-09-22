from generalFunctions import *
from view.entity import *


class BeingView(EntityView):
    """
    display of being
    """

    def __init__(self, model):
        #parent constructor
        EntityView.__init__(self, model)

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

