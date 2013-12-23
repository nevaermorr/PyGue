from utilities.generalFunctions import *
import pygame
from engine.tile import *
from machine.panel import *


class MetaTile(Tile, Panel):
    """
    appearance of tile
    """
    height = 25
    width = 25

    def __init__(self, coordinates_):
        # inherited constructor
        Tile.__init__(self, coordinates_)
        Panel.__init__(self, MetaTile.width, MetaTile.height)
        #visual aspects
        self.ascii = '#'
        self.font_color = pygame.Color(0, 0, 0)
        self.background_color = pygame.Color(20, 20, 20)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 50)

        # create the reel
        self.reel = self.font.render(self.ascii, True, self.font_color)

    def compose_reel(self):
        Panel.compose_reel(self)
        font = self.font.render(self.ascii, True, self.font_color)
        # print centered
        self.reel.blit(font,
                       ((MetaTile.width - font.get_width()) / 2,
                        (MetaTile.height - font.get_height()) / 2)
        )