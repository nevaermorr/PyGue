from generalFunctions import *
from view.entity import *


class BeingView(EntityView):
    """
    display of being
    """

    def __init__(self, model):
        #parent constructor
        EntityView.__init__(self, model)

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

