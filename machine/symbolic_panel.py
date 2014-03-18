from utilities.general_functions import *
import pygame
from machine.panel import *


class SymbolicPanel(Panel):
    """
    common class for elements with symbolic (one character) visualisation on the screen
    """

    # width of one unit (or quantum) for symbolic panels
    pixels_per_unit_width = 25
    # height of one unit (or quantum) for symbolic panels
    pixels_per_unit_height = 25

    def __init__(
            self,
            unit_width=1,
            unit_height=1,
            background_color=pygame.Color(0, 0, 0),
            font_path='utilities/fonts/veteran_typewriter.ttf',
            font_color=pygame.Color(255, 255, 255),
            font_size=45,
            symbol=''
    ):
        """
        creation of the symbolic panel
        """
        # inherited constructor
        Panel.__init__(
            self,
            unit_width * SymbolicPanel.pixels_per_unit_width,
            unit_height * SymbolicPanel.pixels_per_unit_height,
            background_color, font_path, font_color, font_size
        )
        self.symbol = symbol

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        Panel.compose_reel(self)
        font = self.font.render(self.get_symbol(), True, self.get_font_color())
        # print centered
        self.reel.blit(
            font,
            ((self.pixel_width - font.get_width()) / 2,
             (self.pixel_height - font.get_height()) / 2)
        )

    def get_font_color(self):
        """
        obtain proper color for the font
        """
        # by default the color is invariable
        return self.font_color

    def get_symbol(self):
        """
        obtain symbol of this element
        """
        return self.symbol