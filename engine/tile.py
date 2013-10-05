from generalFunctions import *
from engine.inventory import *
from engine.gear import *
from view.tile import *


class Tile(Gear, InventoryInterface):
    """
    quantum of space
    """
    
    def __init__(self, coordinates_):
        #coordinates of this tile in context of location
        self.coordinates_ = coordinates_
        #add inventory
        InventoryInterface.__init__(self)
        #is it possible to step on this tile?
        self.isPassable = True
        #type of terrain
        self.terrain = ''
        #optional pointer to corresponding location, where this tile leads
        self.passage = None
        #assign view
        self.view = TileView(self)

    def getCoordinates(self):
        """
        get coordinates of this tile
        """
        return self.coordinates_