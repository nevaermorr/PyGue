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
        # ascii symbol for the construction
        self.ascii = '#'
        # color of the construction
        self.font_color = pygame.Color(100, 100, 100)