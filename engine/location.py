from utilities.generalFunctions import *
from engine.gear import *


class Location(Gear):
    """
    single location in the game
    """
    
    def __init__(self, grid_):
        """
        create location
        """
        Gear.__init__(self)
        #assign defined grid
        self.grid_ = grid_
        #pointers to all beings in this map
        self.beings_ = []
    
    def getTileByCoordinates(self, coordinates):
        """
        return tile corresponding to given coordinates_
        """
        #negative coordinates_ not allowed
        if coordinates[0] < 0 or coordinates[1] < 0:
            return False
        elif isSet(self.grid_, *coordinates):
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
