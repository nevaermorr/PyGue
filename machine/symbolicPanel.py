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

    def compose_reel(self):
        Panel.compose_reel(self)
        font = self.font.render(self.get_ascii(), True, self.get_font_color())
        # print centered
        self.reel.blit(
            font,
            ((self.width - font.get_width()) / 2,
             (self.height - font.get_height()) / 2)
        )

    def get_font_color(self):
        """
        obtain proper color for the font
        """
        # by default the color is invariable
        return self.font_color

    def get_ascii(self):
        """
        obtain symbol of this element
        """
        return ''