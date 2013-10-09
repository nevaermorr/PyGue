from engine.inventory import *
from controller.tile import *


class Tile(Gear, InventoryInterface):
    """
    quantum of space
    """
    
    def __init__(self, coordinates_):
        Gear.__init__(self)
        #add inventory
        InventoryInterface.__init__(self)
        #coordinates of this tile in context of location
        self.coordinates_ = coordinates_
        #is it possible to step on this tile?
        self.isPassable = True
        #type of terrain
        self.terrain = ''
        #optional pointer to corresponding location, where this tile leads
        self.passage = None
        #assign controller
        self.controller = TileController(self)

    def getCoordinates(self):
        """
        get coordinates of this tile
        """
        return self.coordinates_