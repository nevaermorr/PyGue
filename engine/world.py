from engine.generalFunctions import *


class World:
    """
    class representing the world
    """
    
    def __init__(self):
        """
        creation of the world!
        """
        from engine.time import Time
        
        #initialize some environment
        self.createEnvironment()
        #boolean flag ending the game
        self.gameOver = False
        #starting the great clock
        self.time = Time()

    def run(self):
        """
        main loop running the game
        """
        while not(self.gameOver):
            #time flies
            self.time.passTime()
            #we are giving a chance to act for everything that is eligible for acting
            for animate in self.currentLocation.getAnimates():
                animate.act()
            
            #temporary doomsday established to prevent the game from running infinitely
            if self.time.dayCount == 10:
                self.endGame()
            
    def endGame(self):
        """
        indicating end of the game for the World.run() method
        """
        self.gameOver = True;
        
    def createEnvironment(self):
        """
        here we create some environment for testing purposes
        """
        from engine.map import Map
        from engine.animate import Animate
        
        #a single map will do for now
        self.maps_ = [Map()]
        #pointer to current location
        self.currentLocation = self.maps_[0]
        
        print('a hero is born')
        hero = Animate(self.currentLocation, [0, 0])