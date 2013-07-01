from engine.generalFunctions import *


class Tile:
    """
    class corresponding to quantum of space
    """
    
    def __init__(self):
        #is it possible to step on this tile?
        self.isPassable = True
        #type of terrain
        self.terrain = ''
        #optional pointer to corresponding location, where this tile leads
        self.passage = None
        #list of pointers to present entities
        self.entities_ = []
        #pointer to being present on tile;
        self.being = None
        
    def getBeings(self):
        """
        return all beings present on this tile
        """
        return self.being