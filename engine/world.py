from engine.generalFunctions import *
class World:
    "class representing the world"
    
    def __init__(self):
        "creation of the world!"
        from engine.map import Map
        from engine.time import Time
        
        #a single map will do for now
        self.maps_ = [Map()]
        #pointer to current location
        self.currentLocation = self.maps_[0]
        #boolean flag ending the game
        self.gameOver = False
        #starting the great clock
        self.time = Time()

    def run(self):
        "main loop running the game"
        while (not(self.gameOver)):
            #time flies
            self.time.passTime()
            #we're giving a chance to act for everything that is eligible for acting
            for animate in self.currentLocation.getAnimates():
                animate.act()
            
            #temporary doomsday established to prevent the game from running infinitely
            if self.time.dayCount == 10:
                self.endGame()
            
    def endGame(self):
        "indicating end of the game for the World.run() method"
        self.gameOver = True;