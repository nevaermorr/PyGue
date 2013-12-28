from utilities.generalFunctions import *
import pygame
from engine.door import *


class MetaDoor(Door):
    """
    appearance of wall
    """

    def __init__(self, closed=True):
        # inherited constructor
        Door.__init__(self, closed)
        # default color of the door
        self.font_color = pygame.Color(100, 100, 100)
        # default ascii symbols of the door
        self.ascii_open = '/'
        self.ascii_closed = '+'

    def get_ascii(self):
        if self.closed:
            return self.ascii_closed
        else:
            return self.ascii_open

    def get_font_color(self):
        """
        obtain color of the wall
        """
        return self.font_color