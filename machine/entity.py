from utilities.generalFunctions import *
import pygame
from engine.entity import *


class MetaEntity(Entity):
    """
    appearance of entity
    """

    def compose_reel(self):
        # inherited routine
        Entity.compose_reel(self)
        self.reel.blit(self.font.render(self.ascii, True, self.font_color), (0, 0))