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
        #pointers to all beings in this map
        self.beings_ = []
    
    def getTileByCoordinates(self, coordinates):
        """
        return tile corresponding to given coordinates
        """

        if isSet(self.grid_, *coordinates):
            return self.grid_[coordinates[0]][coordinates[1]]
        else:
            return False
        
    def getBeings(self):
        """
        return all beings present in the location
        """
        return self.beings_

    def checkIn(self, being):
        """
        notice presence of being in this location
        """
        self.beings_.append(being)

    def checkOut(self, exBeing):
        """
        when being leaves the location, forget it
        """
        self.beings_.remove(exBeing)
