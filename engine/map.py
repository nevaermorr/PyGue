from engine.generalFunctions import *
class Map:
    "class corresponding to single location in the game"
    
    def __init__(self):
        "creating map"
        from engine.tile import Tile
        
        #creating example grid
        self.grid_ = [[Tile() for i in range(10)] for j in range(10)]
        
    def validateCoordinates(self, coordinates_):
        "method checks if all desired tiles are not occupied by animated entity"
        pass
    
    def getTileByCoordinates(self, coordinates):
        "methods returns tile corresponding to given coordinates"
        