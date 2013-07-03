from engine.generalFunctions import *
from engine.entity import Entity


class Item(Entity):
    """
    class corresponding to usable items
    """
    def __init__(self, location, coordinates):
        #inherited state
        Entity.__init__(self, location, coordinates)
        #inform tile about presence of new item
        self.location.getTileByCoordinates(coordinates).addItem(self)