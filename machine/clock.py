from utilities.generalFunctions import *
import pygame
from engine.clock import *


class MetaClock(Clock):
    """
    appearance of clock
    """

    def compose_reel(self):

        # inherited routine
        Clock.compose_reel(self)

        time = self.get_time()

        time_string = str(time[2]) + '.' + str(time[3]) + '.' + str(time[4])+', '\
            + str(time[1]) + ':' + str(time[0])
        self.reel = self.font.render(time_string, True, self.font_color)