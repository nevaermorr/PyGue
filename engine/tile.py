from generalFunctions import *
from engine.inventory import *
from engine.gear import *


class Tile(Gear, InventoryInterface):
    """
    quantum of space
    """
    
    def __init__(self):
        #add inventory
        InventoryInterface.__init__(self)
        #is it possible to step on this tile?
        self.isPassable = True
        #species of terrain
        self.terrain = ''
        #optional pointer to corresponding location, where this tile leads
        self.passage = None

    def displayPresentItems(self):
        """
        display items present on this tile
        """
        #if there are any items
        if not self.inventory.isEmpty():
            log('msg', 'found:')
            self.inventory.displayElements()