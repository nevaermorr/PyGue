from utilities.generalFunctions import *
from machine.gear import *


class Clock(MetaGear):
    """
    class representing time passing in the game's world
    """
    
    # equivalence of time units
    quanta_per_hour = 5000
    hour_per_day = 24
    days_per_moon = 30
    moons_per_year = 12
    
    def __init__(self):
        """
        start the great clock
        """
        MetaGear.__init__(self)
        # minimal quantum of time
        self.quantum = 0
        self.hour = 0
        self.day = 0
        self.moon = 0
        self.year = 0
        
    def pass_time(self):
        """
        trigger passing of in-game time
        """
        # increment passed quanta of time
        self.quantum += 1
        # check if full hour have passed
        if self.quantum == Clock.quanta_per_hour:
            self.increment_hour()
        
    def increment_hour(self):
        """
        increment number of hours
        """
        # next hour resets counter of quanta in hour
        self.quantum = 0
        # increment passed hours
        self.hour += 1
        # check if a day have passed
        if self.hour == Clock.hour_per_day:
            self.increment_day()
        
    def increment_day(self):
        """
        increment number of days
        """
        # next day resets counter of hours in day
        self.hour = 0
        # increment passed days
        self.day += 1
        # check if a moon have passed
        if self.day == Clock.days_per_moon:
            self.increment_moon()

    def increment_moon(self):
        """
        increment number of moons
        """
        # next moon resets counter of days in moon
        self.day = 0
        # increment passed moons
        self.moon += 1
        # check if a year have passed
        if self.day == Clock.days_per_moon:
            self.increment_year()

    def increment_year(self):
        """
        increment number of years
        """
        # next year resets counter of moons in year
        self.moon = 0
        # increment passed years
        self.year += 1

    def get_full_datetime(self):
        """
        get all numbers denoting game-time
        """
        return self.quantum, self.hour, self.day, self.moon, self.year

    def get_simplified_time(self):
        """
        get current game time in format hh:mm
        """
        return '{:02.0f}:{:02.0f}'.format(self.hour, (60 * self.quantum / self.quanta_per_hour))

    def get_simplified_date(self):
        """
        get current date in format dd/mm/yyyy
        """
        return '{:02.0f}/{:02.0f}/{:04.0f}'.format(self.day, self.moon, self.year)