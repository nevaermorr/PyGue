from engine.generalFunctions import *
class Map:
    "class corresponding to single location in the game"
    
    def __init__(self):
        "creating map"
        from engine.tile import Tile
        
        #creating example grid
        self.grid_ = [[Tile() for i in range(10)] for j in range(10)]
        #pointers to all animate entities in this map
        self.animates_ = []
    
    def getTileByCoordinates(self, coordinates):
        "method returns tile corresponding to given coordinates"
        if isset(self.grid_, coordinates):
            return self.grid_[coordinates[0]][coordinates[1]]
        else:
            return False
        
    def getAnimates(self):
        return self.animates_