from generalFunctions import *
from engine.entity import *
from view.item import *


class Item(Entity):
    """
    usable item
    """

    def __init__(self, location, coordinates_):
        #inherited state
        Entity.__init__(self, location, coordinates_)
        #inform tile about presence of new item
        self.getCurrentTile().addItems(self)
        #assing view
        self.view=ItemView(self)