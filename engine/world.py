from engine.generalFunctions import *
class World:
    "class representing the world"
    from engine.generalFunctions import isset
    
    def __init__(self):
        "creation of the world!"
        from engine.map import Map
        
        #a single map will do for now
        self.maps_ = [Map()]
        
        #boolean flag ending the game
        self.gameOver = False

    def run(self):
        "main loop running the game"
        while (not(self.gameOver)):
            self.endGame()
            
    def endGame(self):
        "indicating end of the game for the World.run() method"
        self.gameOver = True;