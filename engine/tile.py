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