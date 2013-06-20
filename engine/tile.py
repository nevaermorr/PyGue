from engine.generalFunctions import *
class Tile:
    "class corresponding to quantum of space"
    
    def __init__(self):
        #is it possible to step on this tile?
        self.isPassable = True
        #type of terrain
        self.terrain = ""
        #optional pointer to corresponding location, where this tile leads
        self.passage = None
        