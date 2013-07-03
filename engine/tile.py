from engine.generalFunctions import *


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
        #list of pointers to present items
        self.items_ = []
        #pointer to being present on tile
        self.being = None
        
    def getAnimates(self):
        """
        return all animate entities present on this tile
        """
        return self.animates_

    def displayPresentItems(self):
        #if there are any items
        if self.items_:
            log('msg', 'found:')
            for item in self.items_:
                log('msg', 'some item')

    def addItem(self, item):
        """
        add item to the list of items present on this tile
        """
        self.items_.append(item)

    def removeItem(self, item):
        """
        remove item to the list of items present on this tile
        """
        self.items_.remove(item)