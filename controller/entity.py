from controller.controller import *


class EntityController(Controller):
    """
    display of entity
    """

    def __init__(self, model):
        #parent constructor
        Controller.__init__(self, model)
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