from engine.gear import *


class Time(Gear):
    """
    class representing time passing in the game's world
    """
    
    # equivalence of time units
    quanta_per_hour = 1000
    hour_per_day = 24
    days_per_moon = 30
    
    def __init__(self):
        """
        start the great clock
        """
        Gear.__init__(self)
        self.quantum_count = 0
        self.quantum_of_hour = 0
        self.hour_count = 0
        self.hour_of_day = 0
        self.day_count = 0
        self.day_of_moon = 0
        self.moon_count = 0
        
    def pass_time(self):
        """
        trigger passing of in-game time
        """
        # incrementing passed quanta of time
        self.quantum_count += 1
        self.quantum_of_hour += 1
        # checking if full hour have passed
        if self.quantum_of_hour == Time.quanta_per_hour:
            self.increment_hour()
        
    def increment_hour(self):
        """
        increment number of hours
        """
        # next hour resets counter of quanta in hour
        self.quantum_of_hour = 0
        # incrementing passed hours
        self.hour_count += 1
        self.hour_of_day += 1
        # checking if a day have passed
        if self.hour_of_day == Time.hour_per_day:
            self.increment_day()
        
    def increment_day(self):
        """
        increment number of days
        """
        # next day resets counter of hours in day
        self.hour_of_day = 0
        # incrementing passed days
        self.day_count += 1

    def get_current_time(self):
        """
        compose string with formatted game-time
        """
        return (str(self.hour_of_day) + ':' + str(self.quantum_of_hour) + ' '
              + str(self.day_count) + '/' + str(self.moon_count))