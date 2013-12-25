from utilities.generalFunctions import *
import pygame
from machine.panel import *


class SymbolicPanel(Panel):
    """
    common class for elements with visualisation on the screen
    """

    def __init__(
            self, width, height,
            background_color=pygame.Color(0, 0, 0),
            font_path='utilities/fonts/veteran_typewriter.ttf',
            font_color=pygame.Color(255, 255, 255),
            font_size=45):
        # inherited constructor
        Panel.__init__(self, width, height, background_color, font_path, font_color, font_size)

        #ascii symbol of the element
        self.ascii = ''

    def compose_reel(self):
        Panel.compose_reel(self)
        font = self.font.render(self.ascii, True, self.font_color)
        # print centered
        self.reel.blit(font,
                       ((self.width - font.get_width()) / 2,
                        (self.height - font.get_height()) / 2)
        )