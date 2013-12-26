from utilities.generalFunctions import *
import pygame
from engine.clock import *


class MetaClock(Clock):
    """
    appearance of clock
    """

    def __init__(self):
        # inherited constructor
        Clock.__init__(self)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 25)
        self.reel = pygame.Surface((100, 50))

    def compose_reel(self):

        # inherited routine
        Clock.compose_reel(self)

        #time = self.get_full_datetime()
        #
        #time_string = str(time[2]) + '.' + str(time[3]) + '.' + str(time[4])+', '\
        #    + str(time[1]) + ':' + str(time[0])
        #self.reel = self.font.render(time_string, True, self.font_color)

        time_text = self.font.render(self.get_simplified_time(), True, self.font_color)
        self.reel.blit(time_text, [0, 0])
        date_text = self.font.render(self.get_simplified_date(), True, self.font_color)
        self.reel.blit(date_text, [0, 25])