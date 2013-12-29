from utilities.generalFunctions import *
import pygame
from engine.clock import *


class MetaClock(Clock):
    """
    complement of clock
    """

    def __init__(self):
        """
        creation of clock
        """
        # inherited constructor
        Clock.__init__(self)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 25)
        self.reel = pygame.Surface((100, 50))

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # inherited routine
        Clock.compose_reel(self)

        time_text = self.font.render(self.get_simplified_time(), True, self.font_color)
        self.reel.blit(time_text, [0, 0])
        date_text = self.font.render(self.get_simplified_date(), True, self.font_color)
        self.reel.blit(date_text, [0, 25])

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