from engine.generalFunctions import *
class Time:
    "class representing time passing in the game's world"
    
    #number of time quanta per hour
    quantaPerHour = 1000
    
    def __init__(self):
        "starting the great clock"
        self.quantumCount = 0
        self.quantumOfHour = 0
        self.hourCount = 0
        self.hourOfDay = 0
        self.dayCount = 0
        self.dayOfMoon = 0
        self.moonCount = 0
        
    def passTime(self):
        "method that triggers passing of in-game time"
        #incrementing passed quanta of time
        self.quantumCount += 1
        self.quantumOfHour += 1
        #checking if full hour have passed
        if self.quantumOfHour == self.quantaPerHour:
            self.incrementHour()
        
    def incrementHour(self):
        "method that increments hour"
        #next hour resets counter of quanta in hour
        self.quantumOfHour = 0
        #incrementing passed hours
        self.hourCount += 1
        self.hourOfDay += 1
        #checking if a day have passed
        if self.hourOfDay == 24:
            self.incrementDay()
        
    def incrementDay(self):
        "method that increments day"
        #next day resets counter of hours in day
        self.hourOfDay = 0
        #incrementing passed days
        self.dayCount += 1