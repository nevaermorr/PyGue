from utilities.generalFunctions import *
from machine.gear import *


class Location(MetaGear):
    """
    single location in the game
    """
    
    def __init__(self, tiles_):
        """
        create location
        :param tiles_: tiles constituting the location
        """
        MetaGear.__init__(self)
        # assign defined grid
        self.tiles_ = tiles_
        # pointers to all beings in this map
        self.beings_ = []
        # additional pointer to hero (if present)
        self.hero = None

    def get_tile_by_coordinates(self, x, y):
        """
        return tile corresponding to given coordinates
        :param x: horizontal coordinate of tile
        :param y: vertical coordinate of tile
        """
        # negative coordinates not allowed
        if x < 0 or y < 0:
            return False
        elif is_set(self.tiles_, x, y):
            return self.tiles_[x][y]
        else:
            return False
        
    def get_beings(self):
        """
        return all beings present in the location
        """
        return self.beings_

    def get_hero(self):
        """
        obtain pointer to hero if present in this location
        """
        return self.hero

    def check_in(self, being):
        """
        notice presence of being in this location
        :param being: being which enters the location
        """
        self.beings_.append(being)
        # for hero store another pointer
        if type(being).__name__ == 'MetaHero':
            self.hero = being

    def check_out(self, being):
        """
        when being leaves the location, forget it
        :param being: being which leaves the location
        """
        self.beings_.remove(being)
        # hero need special additional treatment
        if type(being).__name__ == 'MetaHero':
            self.hero = None
