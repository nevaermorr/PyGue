from engine.generalFunctions import *
from engine.being import Being


class Hero(Being):
    """
    player character
    """

    def __init__(self, location, coordinates, species):
        Being.__init__(self, location, coordinates, species)
        #log information about hero's birth
        log('msg', 'a hero is born')

    def chooseAction(self):
        """
        choose action basing on players input
        """
        import sys
        from data.keyMapping import keyMapping_

        actionKey = sys.stdin.readlines(1)[0][0]
        #wait for valid command
        while not isSet(keyMapping_, actionKey):
            log('warning', 'unknown action')
            actionKey = sys.stdin.readlines(1)[0][0]
        #return corresponding method name
        return keyMapping_[actionKey]

    @doc_inherit
    def performAction(self, actionName, *actionParameters_):
        result = Being.performAction(self, actionName, *actionParameters_)
        #try to log corresponding message
        self.msg(actionName)
        #return original result
        return result

    @doc_inherit
    def loadSpeciesDependencies(self, species):
        Being.loadSpeciesDependencies(self, species)
        #only heroes can quit
        self.actionTimeCosts_['quit'] = 0

    def quit(self):
        """
        quit the game
        """
        #the world is a cold place now
        from engine.world import World
        World.gameOver = True
        #successful quit
        return True

    def die(self):
        """
        what happens when hero dies
        """
        Being.die(self)
        #leave it all behind
        self.quit()

    def move(self, direction):
        #move like other beings
        #if movement failed
        if not Being.move(self, direction):
            #report failure of movement
            return False
        #if movement succeeded
        else:
            #display stuff found at current tile
            self.location.getTileByCoordinates(self.coordinates).displayPresentItems()
            #in the end report success of movement
            return True
