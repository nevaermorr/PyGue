from engine.gear import *
from engine.time import *
from controller.world import *

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

        Gear.__init__(self)
        #initialize some environment
        self.createEnvironment()
        #start the great clockWorld
        self.time = Time()
        #link world with its switch
        self.switch = WorldSwitch(self)

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
        #notify the switch about end of the game
        self.switch.callEndGame()

    def createEnvironment(self):
        """
        create some environment for testing purposes
        """
        from data.environment.testEnvironment import initEnvironment

        #a single map will do for now
        self.locations_ = initEnvironment()
        #pointer to current location
        self.currentLocation = self.locations_[0]