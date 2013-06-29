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

        actionKey = sys.stdin.readlines(1)[0][0]
        if actionKey == 'q':
            return['quit']
        if actionKey == '1':
            return ['move', 'SW']
        if actionKey == '2':
            return ['move', 'S']
        if actionKey == '3':
            return ['move', 'SE']
        if actionKey == '4':
            return ['move', 'W']
        if actionKey == '6':
            return ['move', 'E']
        if actionKey == '7':
            return ['move', 'NW']
        if actionKey == '8':
            return ['move', 'N']
        if actionKey == '9':
            return ['move', 'NE']
        #default action is a pass
        return None

    def quit(self):
        """
        quit the game
        """
        #the world is a cold place now
        from engine.world import World
        World.gameOver = True

    def die(self):
        """
        hero have fallen during his quest
        """
        Animate.die(self)
        self.quit()