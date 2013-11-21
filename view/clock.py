from utilities.generalFunctions import *
from view.panel import *
import pygame


class ClockPanel(Panel):
    """
    appearance of clock
    """

    def __init__(self, clock_switch):
        Panel.__init__(self, clock_switch)

    def compose_reel(self):
        time = self.switch.get_time()

        time_string = str(time[2]) + '.' + str(time[3]) + '.' + str(time[4])+', '\
            + str(time[1]) + ':' + str(time[0])
        self.reel = self.font.render(time_string, True, self.font_color)