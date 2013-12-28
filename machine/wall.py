from utilities.generalFunctions import *
import pygame
from engine.wall import *


class MetaWall(Wall):
    """
    appearance of wall
    """

    def __init__(self):
        # inherited constructor
        Wall.__init__(self)
        # default color of the wall
        self.font_color = pygame.Color(100, 100, 100)
        # default ascii symbol of the wall
        self.ascii = '#'

    def get_font_color(self):
        """
        obtain color of the wall
        """
        return self.font_color

    def get_ascii(self):
        """
        ascii symbol for the construction
        """
        return self.ascii