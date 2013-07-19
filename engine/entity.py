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
        #import default messages characteristic to this entity
        self._importDefaults()

    def _importDefaults(self):
        """
        import all defaults for this entity
        """
        try:
            module = __import__('data.' + self.__class__.__name__.lower() + '.default',
                                fromlist=['messages_'])
            self.messages_ = module.messages_
        #warn if no default messages are found
        except ImportError:
            self.messages_ = {}
            log('warning', 'no default messages for ' + self.__class__.__name__)

    def msg(self, label):
        """
        log message characteristic to this entity
        """
        #log only if specific message is defined for certain label
        if isSet(self.messages_, label):
            log('msg', self.messages_[label])

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
        return self.location.getTileByCoordinates(self.coordinates)

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