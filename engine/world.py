from engine.generalFunctions import *


class World:
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

        #initialize some environment
        self.createEnvironment()
        #start the great clock
        self.time = Time()

    def run(self):
        """
        main loop running the game
        """
        while not World.gameOver:
            #time flies
            self.time.passTime()
            #we are giving a chance to act for everything that is eligible for acting
            for being in self.currentLocation.getBeings():
                being.act()
                #no point in letting anyone act if the game is over
                if World.gameOver:
                    break
            #temporary doomsday established to prevent the game from running infinitely
            if self.time.dayCount == 10:
                break
        #game over here
        else:
            self.endGame()

    def endGame(self):
        """
        indicate end of the game for the World.run() method
        """
        log('msg', self.time.getCurrentTime())

    def createEnvironment(self):
        """
        create some environment for testing purposes
        """
        from data.environment.testEnvironment import initEnvironment

        #a single map will do for now
        self.locations_ = initEnvironment()
        #pointer to current location
        self.currentLocation = self.locations_[0]