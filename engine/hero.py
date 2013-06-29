from engine.generalFunctions import *
from engine.animate import Animate


class Hero(Animate):
    """
    class representing player character
    """
    def chooseAction(self):
        """
        method chooses action based on players input
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
    def loadTypeDependencies(self, type):
        Animate.loadTypeDependencies(self, type)
        #only heroes can quit
        self.actionTimeCosts_['quit'] = 0

    def quit(self):
        """
        quit the game
        """
        #the world is a cold place now
        from engine.world import World
        World.gameOver = True

        return 0

    def die(self):
        """
        hero have fallen during his quest
        """
        Animate.die(self)
        #leave it all behind
        self.quit()