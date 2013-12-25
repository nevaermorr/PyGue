from utilities.generalFunctions import *
import pygame
from engine.entity import *
from machine.symbolicPanel import *


class MetaEntity(Entity, SymbolicPanel):
    """
    appearance of entity
    """

    def __init__(self, location, coordinates_):
        Entity.__init__(self, location, coordinates_)
        SymbolicPanel.__init__(self, self.width, self.height)

    def compose_reel(self):
        # inherited routine
        Entity.compose_reel(self)
        self.reel.blit(self.font.render(self.ascii, True, self.font_color), (0, 0))