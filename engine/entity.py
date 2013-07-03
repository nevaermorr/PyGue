from engine.generalFunctions import *


class Entity:
    """
    any entity present in the in-game world
    """

    def __init__(self, location, coordinates):
        """
        creation of entity
        :param location: location where the entity is placed
        :param coordinates: coordinates depicting the position of entity in given location
        """
        #pointer to the map, where this entity is currently present
        self.location = location
        #coordinates of the tile, on which this entity is located
        self.coordinates = coordinates
        #size of entity (length of one side in tiles)
        self.size = 1
        #ASCII character representing the entity
        self.character = ''

    def move(self, direction):
        """
        what happens when some force moves the entity
        :param direction: direction of the movement given as literal geographic direction
        """
        #evaluate desired position
        vector = directionToVector(direction)
        newCoordinates = [self.coordinates[0] + vector[0], self.coordinates[1] + vector[1]]
        #check if new position is available
        if self.canMoveTo(newCoordinates):
            #move to new position
            self.coordinates = newCoordinates
            log('msg', 'entity moves to', newCoordinates)
            #report successful movement
            return True
        else:
            log('warning', 'cannot move to', newCoordinates)
            #report movement failure
            return False

    def moveAlongPath(self, path):
        """
        execute movement to subsequent points of route
        :param path: list of directions of consecutive steps
        """
        pass

    def canMoveTo(self, coordinates):
        """
        check if certain position in the location is accessible for this entity
        :param coordinates: coordinates of desired position
        """
        #find corresponding tile
        targetTile = self.location.getTileByCoordinates(coordinates)

        #check if tile exists and is accessible
        if (
            targetTile
            and targetTile.isPassable
        ):
            return True
        else:
            return False

#===========
#pseudo-static methods


def directionToVector(direction):
        """
        translate direction in form of string into vector
        :param direction: literal geographical direction, combination of N, W, S, E
        """
        vector = [0, 0]
        if direction.find("N") > -1:
            vector[1] = 1
        if direction.find("S") > -1:
            vector[1] = -1
        if direction.find("E") > -1:
            vector[0] = 1
        if direction.find("W") > -1:
            vector[0] = -1
        return vector