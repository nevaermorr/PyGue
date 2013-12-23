from utilities.generalFunctions import *
from machine.gear import *


class Entity(MetaGear):
    """
    any entity present in the in-game world
    """

    def __init__(self, location, coordinates_):
        """
        creation of entity
        :param location: location where the entity is placed
        :param coordinates_: coordinates depicting the position of entity in given location
        """

        MetaGear.__init__(self)
        # pointer to the map, where this entity is currently present
        self.location = location
        # coordinates_ of the tile, on which this entity is located
        self.coordinates_ = coordinates_
        # size of entity (length of one side measured in tiles)
        self.size = 1

    def move(self, direction_):
        """
        what happens when some force moves the entity
        :param direction_: direction of the movement given as [x,y] vector
        """
        # evaluate desired position
        new_coordinates_ = [self.coordinates_[0] + direction_[0],
                            self.coordinates_[1] + direction_[1]]
        # check if new position is available
        if self.can_move_to(new_coordinates_):
            # move to new position
            self.coordinates_ = new_coordinates_
            # report successful movement
            return True
        else:
            # report movement failure
            return False

    def can_move_to(self, coordinates_):
        """
        check if certain position in the location is accessible for this entity
        :param coordinates_: coordinates of desired position
        """
        # find corresponding tile
        target_tile = self.location.get_tile_by_coordinates(coordinates_)

        # check if tile exists and is accessible
        if (
            target_tile
            and target_tile.is_passable
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
        return self.location.get_tile_by_coordinates(self.coordinates_)

    def get_coordinates(self):
        """
        accessor for coordinates
        """
        return self.coordinates_

    def get_x(self):
        """
        get coordinate from x-axis
        """
        return self.coordinates_[0]

    def get_y(self):
        """
        get coordinate from x-axis
        """
        return self.coordinates_[1]