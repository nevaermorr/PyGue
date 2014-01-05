from utilities.generalFunctions import *
from machine.inventory import *


class Tile(MetaInventoryInterface):
    """
    quantum of space
    """

    def __init__(self, coordinates_):
        """
        creation of tile
        :param coordinates_: coordinates of the tile relative to the location
        """
        # add inventory
        MetaInventoryInterface.__init__(self)
        # coordinates of this tile in context of location
        self.coordinates_ = coordinates_
        # type of terrain
        self.terrain = ''
        # optional pointer to corresponding location, to where this tile leads
        self.passage = None
        # constructional element on this tile
        self.construction = None
        # has the hero ever seen this tile?
        self.visited = False
        # is the tile it visible for hero?
        # -1 = uncharted
        # 0 = darkness
        # 1 = shadow
        # 2 = visible
        self.visible = -1

    def is_passable(self):
        """
        check if it is possible to pass through this tile
        """
        # if there is some constructional element it determines the passability of the tile
        if self.construction:
            return self.construction.is_passable()
        # otherwise it is determined by the tile's natural passability;
        # by default tile is passable
        return True

    def get_visibility(self):
        """
        check if the tile is in hero's field of view
        """
        # if this check is performed, tile is considered as visited
        if self.visible:
            self.visited = True

        if not self.visited:
            return -1
        # return the result
        return self.visible

    def calculate_visibility(self, hero):
        """
        examine if given tile is in sight of hero
        :param hero: pointer to said hero
        """

        # squared distance between hero and the tile
        sq_distance = (hero.get_x() - self.get_x()) ** 2\
                       + (hero.get_y() - self.get_y()) ** 2

        sq_range_ = hero.get_square_range_of_view()
        # clearly visible
        if sq_distance < sq_range_['visible']:
            self.visible = 2
        # barely visible
        elif sq_distance < sq_range_['shadow']:
            self.visible = 1
        # not visible (but already has been seen)
        elif self.visible != -1:
            self.visible = 0
        # still never seen
        else:
            self.visible = -1

    def get_coordinates(self):
        """
        get coordinates of this tile
        """
        return self.coordinates_

    def get_x(self):
        """
        get coordinate from x-axis
        """
        return self.coordinates_[0]

    def get_y(self):
        """
        get coordinate from y-axis
        """
        return self.coordinates_[1]

    def get_construction(self):
        """
        obtain access to construction present on this tile (if any)
        """
        return self.construction