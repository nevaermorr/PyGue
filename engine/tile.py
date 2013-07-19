from engine.generalFunctions import *
from engine.inventory import Inventory


class Tile:
    """
    class corresponding to quantum of space
    """
    
    def __init__(self):
        #is it possible to step on this tile?
        self.isPassable = True
        #species of terrain
        self.terrain = ''
        #optional pointer to corresponding location, where this tile leads
        self.passage = None
        #inventory object for present items
        self.inventory = Inventory(self)
        #pointer to being present on tile
        self.being = None

    def displayPresentItems(self):
        #if there are any items
        if not self.inventory.isEmpty():
            log('msg', 'found:')
            for item in self.inventory.get():
                log('msg', str(item))

    def addItems(self, *items_):
        """
        add item to the list of items present on this tile
        """
        self.inventory.add(*items_)

    def removeItem(self, item):
        """
        remove item to the list of items present on this tile
        """
        self.inventory.removeItems(item)