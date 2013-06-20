from engine.generalFunctions import *
class Entity:
    "class corresponding to all entities present in the in-game world"
    
    def __init__(self, coordinates):
        "creation of entity"
        #pointer to the map, where this entity is currently present
        self.location = None
        #coordinates of the tile, on which this entity is located
        self.coordinates = coordinates
        #size of entity (length of one side in tiles)
        self.size = 1
        #ASCII character representing the entity
        self.character = ""
        
    def move(self, direction):
        "what happens when some force moves the entity"
        #vector of movement
        vector = directionToVector(direction)
        #checking if new position is available
        newCoordinates = [self.coordinates[0] + vector[0], self.coordinates[1] + vector[1]]
#        if self.canMoveTo(tile)
        #changing current coordinates
        self.coordinates = newCoordinates
        
    def moveAlongPath(self, path):
        "executing movement to subsequent points of route"
        pass
    
    def canMoveTo(self, tile):
        "checking if certain tile is accessible for this entity"
        #by default we allow entity to move to any accessible tile
        if tile.accessible == True:
            return True
        else:
            return False
            
#==========
#pseudo-static methods  
        
def directionToVector(direction):
        "function translates direction in form of string into vector"
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