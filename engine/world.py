from generalFunctions import *
from engine.gear import *


class World(Gear):
    """
    the game universe
    """
    #boolean flag ending the game
    gameOver = False

    def __init__(self):
        """
        creation of the world!
        """
        from engine.time import Time
        from view.world import WorldView

        #link world with its view
        self.view = WorldView(self)
        #initialize some environment
        self.createEnvironment()
        #start the great clockWorld
        self.time = Time()

    def run(self):
        """
        main loop running the game
        """
        while not World.gameOver:
            #time flies
            self.time.passTime()
            #give a chance to act for everything that is eligible for acting
            for being in self.currentLocation.getBeings():
                being.act()
                #no point in letting anyone act if the game is over
                if World.gameOver:
                    break
        #game over here
        else:
            self.endGame()

    def endGame(self):
        """
        manage everything that needs to be done once the game come to its end
        """
        #notify the view about end of the game
        self.view.callEndGame()

    def createEnvironment(self):
        """
        create some environment for testing purposes
        """
        from data.environment.testEnvironment import initEnvironment

        #a single map will do for now
        self.locations_ = initEnvironment()
        #pointer to current location
        self.currentLocation = self.locations_[0]