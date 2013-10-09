from engine.gear import *
from controller.entity import *


class Entity(Gear):
    """
    any entity present in the in-game world
    """

    def __init__(self, location, coordinates_):
        """
        creation of entity
        :param location: location where the entity is placed
        :param coordinates_: coordinates depicting the position of entity in given location
        """

        Gear.__init__(self)
        #pointer to the map, where this entity is currently present
        self.location = location
        #coordinates_ of the tile, on which this entity is located
        self.coordinates_ = coordinates_
        #size of entity (length of one side measured in tiles)
        self.size = 1
        #assign the controller
        self.controller = EntityController(self)

    def move(self, direction_):
        """
        what happens when some force moves the entity
        :param direction_: direction of the movement given as literal geographic direction
        """
        #evaluate desired position
        newCoordinates_ = [self.coordinates_[0] + direction_[0], self.coordinates_[1] + direction_[1]]
        #check if new position is available
        if self.canMoveTo(newCoordinates_):
            #move to new position
            self.coordinates_ = newCoordinates_
            #report successful movement
            return True
        else:
            self.controller.callActionMove(False)
            #report movement failure
            return False

    def canMoveTo(self, coordinates_):
        """
        check if certain position in the location is accessible for this entity
        :param coordinates_: coordinates of desired position
        """
        #find corresponding tile
        targetTile = self.location.getTileByCoordinates(coordinates_)

        #check if tile exists and is accessible
        if (
            targetTile
            and targetTile.isPassable
        ):
            return True
        else:
            self.controller.callActionCanMoveTo(False, targetTile)
            return False

    def __str__(self):
        """
        description of this entity
        """
        #by default assign class name as description
        return self.__class__.__name__

    def getCurrentTile(self):
        """
        method retrieves tile on which the entity is located
        :rtype : Tile
        """
        return self.location.getTileByCoordinates(self.coordinates_)

    def getCoordinates(self):
        """
        accessor for coordinates
        """
        return self.coordinates_