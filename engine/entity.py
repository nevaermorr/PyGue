from engine.generalFunctions import *


class Entity:
    """
    class corresponding to all entities present in the in-game world
    """
    
    def __init__(self, location, coordinates):
        """
        creation of entity
        :param location: location where the Entity is placed
        :param coordinates: coordinates depicting the position of Entity in given location
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
        #evaluation of desired position
        vector = directionToVector(direction)
        newCoordinates = [self.coordinates[0] + vector[0], self.coordinates[1] + vector[1]]
        destinationTile = self.location.getTileFromCoordinates(newCoordinates)
        #checking if new position is available
        if self.canMoveTo(destinationTile):
            #moving to new position
            self.coordinates = newCoordinates
        
    def moveAlongPath(self, path):
        """
        executing movement to subsequent points of route
        :param path: list of directions of consecutive steps
        """
        pass
    
    def canMoveTo(self, tile):
        """
        checking if certain tile is accessible for this entity
        :param tile: tile in question
        """
        #by default we allow entity to move to any accessible tile
        if tile.accessible:
            return True
        else:
            return False
            
#==========
#pseudo-static methods


def directionToVector(direction):
        """
        function translates direction in form of string into vector
        :param direction: literal geographical direction, combination of N, W, S, E
        """
        vector = [0, 0]
        if direction.find("N") > -1:
            vector[0] = 1
        if direction.find("S") > -1:
            vector[0] = -1
        if direction.find("E") > -1:
            vector[1] = 1
        if direction.find("W") > -1:
            vector[1] = -1
        return vector