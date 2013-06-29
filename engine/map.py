from engine.generalFunctions import *


class Map:
    """
    class corresponding to single location in the game
    """
    
    def __init__(self):
        """
        create map
        """
        from engine.tile import Tile
        
        #creating example grid
        self.grid_ = [[Tile() for i in range(10)] for j in range(10)]
        #pointers to all animate entities in this map
        self.animates_ = []
    
    def getTileByCoordinates(self, coordinates):
        """
        return tile corresponding to given coordinates
        """

        if isSet(self.grid_, *coordinates):
            return self.grid_[coordinates[0]][coordinates[1]]
        else:
            return False
        
    def getAnimates(self):
        """
        return all animate entities present in the location
        """
        return self.animates_

    def checkIn(self, animate):
        """
        notice presence of animate entity in this location
        """
        self.animates_.append(animate)

    def checkOut(self, exAnimate):
        """
        when entity leaves the location, forget it
        """
        self.animates_.remove(exAnimate)
