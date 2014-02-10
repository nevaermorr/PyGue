from utilities.general_functions import *
import pygame
from engine.door import *


class MetaDoor(Door):
    """
    complement of wall
    """

    def __init__(self, opened=False):
        """
        creation of door
        """
        # inherited constructor
        Door.__init__(self, opened)
        # default color of the door
        self.font_color = pygame.Color(100, 100, 100)
        # default ascii symbols of the door
        self.ascii_opened = '/'
        self.ascii_closed = '+'

    def get_symbol(self):
        """
        obtain symbol of the wall
        """
        # symbol of the door depends whether it is open or closed
        if self.opened:
            return self.ascii_opened
        else:
            return self.ascii_closed

    def get_font_color(self):
        """
        obtain color of the wall
        """
        # return default color
        return self.font_color