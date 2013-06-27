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
        #list of animate entities present on tile;
        #for convenience kept apart from non-animate entities
        self.animates_ = []
        
    def getAnimates(self):
        """
        return all animate entities present on this tile
        """
        return self.animates_