from engine.generalFunctions import *
from engine.being import Being


class Hero(Being):
    """
    player character
    """
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
        #log some notice about hero's death
        log('msg', 'hero have fallen during his quest')
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
            #TODO display stuff found at current tile
            #in the end report success of movement
            return True
