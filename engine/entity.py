from utilities.generalFunctions import *
from machine.gear import *
from machine.spatial import *


class Entity(MetaGear, MetaSpatial):
    """
    any entity present in the in-game world
    """

    def __init__(self, location, x, y):
        """
        creation of entity
        :param location: location where the entity is placed
        :param x: horizontal coordinate
        :param y: vertical coordinate
        """

        # inherited constructors
        MetaGear.__init__(self)
        MetaSpatial.__init__(self, x, y)
        # pointer to the map, where this entity is currently present
        self.location = location
        # size of entity (length of one side measured in tiles)
        self.size = 1

    def move(self, direction_):
        """
        what happens when some force moves the entity
        :param direction_: direction of the movement given as [x,y] vector
        """
        # evaluate desired position
        x = self.x + direction_[0]
        y = self.y + direction_[1]
        # check if new position is available
        if self.can_move_to(x, y):
            # move to new position
            self.x = x
            self.y = y
            # report successful movement
            return True
        else:
            # report movement failure
            return False

    def can_move_to(self, x, y):
        """
        check if certain position in the location is accessible for this entity
        :param x: horizontal coordinate of desired position
        :param y: vertical coordinate of desired position
        """
        # find corresponding tile
        target_tile = self.location.get_tile_by_coordinates(x, y)

        # check if tile exists and is accessible
        if (
            target_tile
            and target_tile.is_passable()
        ):
            return True
        else:
            return False

    def __str__(self):
        """
        description of this entity
        """
        # by default assign class name as description
        return self.__class__.__name__

    def get_current_tile(self):
        """
        method retrieves tile on which the entity is located
        :rtype : Tile
        """
        return self.location.get_tile_by_coordinates(self.x, self.y)