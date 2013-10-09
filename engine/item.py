from engine.entity import *
from controller.item import *


class Item(Entity):
    """
    usable item
    """

    def __init__(self, location, coordinates_):
        #inherited state
        Entity.__init__(self, location, coordinates_)
        #inform tile about presence of new item
        self.getCurrentTile().addItems(self)
        #assing controller
        self.controller=ItemController(self)