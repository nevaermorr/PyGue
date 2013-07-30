from engine.generalFunctions import *
from engine.entity import Entity


class Item(Entity):
    """
    usable item
    """
    def __init__(self, location, coordinates):
        #inherited state
        Entity.__init__(self, location, coordinates)
        #inform tile about presence of new item
        self.getCurrentTile().addItems(self)

    def __str__(self):
        """
        description of the item
        """
        return 'some item'