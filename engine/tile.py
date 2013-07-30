from engine.generalFunctions import *
from engine.inventory import *


class Tile(InventoryInterface):
    """
    class corresponding to quantum of space
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
        #pointer to being present on tile
        self.being = None

    def displayPresentItems(self):
        #if there are any items
        if not self.inventory.isEmpty():
            log('msg', 'found:')
            for item in self.inventory.chooseAll():
                log('msg', str(item))