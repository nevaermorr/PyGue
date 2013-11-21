from utilities.generalFunctions import *
from engine.gear import *
from controller.location import *


class Location(Gear):
    """
    single location in the game
    """
    
    def __init__(self, grid_):
        """
        create location
        """
        Gear.__init__(self)
        # assign defined grid
        self.grid_ = grid_
        # pointers to all beings in this map
        self.beings_ = []
        # link location with its switch
        self.switch = LocationSwitch(self)

    def get_tile_by_coordinates(self, coordinates_):
        """
        return tile corresponding to given coordinates
        """
        # negative coordinates not allowed
        if coordinates_[0] < 0 or coordinates_[1] < 0:
            return False
        elif is_set(self.grid_, *coordinates_):
            return self.grid_[coordinates_[0]][coordinates_[1]]
        else:
            return False
        
    def get_beings(self):
        """
        return all beings present in the location
        """
        return self.beings_

    def check_in(self, being):
        """
        notice presence of being in this location
        """
        self.beings_.append(being)

    def check_out(self, being):
        """
        when being leaves the location, forget it
        """
        self.beings_.remove(being)
