from utilities.generalFunctions import *
from machine.inventory import *
from machine.spatial import *


class Tile(MetaInventoryInterface, MetaSpatial):
    """
    quantum of space
    """

    def __init__(self, x, y):
        """
        creation of tile
        :param x: horizontal coordinate of the tile relative to the location
        :param y: vertical coordinate of the tile relative to the location
        """
        # inherited constructors
        MetaSpatial.__init__(self, x, y)
        # add inventory
        MetaInventoryInterface.__init__(self)
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
        # in range, but view is blocked
        if sq_distance < sq_range_['shadow'] and not hero.in_line_of_sight(self):
            # not visible (but already has been seen)
            if self.visible != -1:
                self.visible = 0
            # still never seen
            else:
                self.visible = -1

        # clearly visible
        elif sq_distance < sq_range_['visible']:
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

    def get_construction(self):
        """
        obtain access to construction present on this tile (if any)
        """
        return self.construction

    def is_transparent(self):
        """
        is it possible to see through this tile?
        """
        # if there is nothing that could block the way
        if not self.construction:
            return True
        # otherwise the obstacle determines its transparency
        else:
            return self.construction.is_transparent()