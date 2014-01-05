from utilities.generalFunctions import *
import pygame
from engine.construction import *


class MetaConstruction(Construction):
    """
    complement of the construction
    """

    def __init__(self, sort=''):
        """
        creation of the construction
        """
        # inherited constructor
        Construction.__init__(self, sort)

    def get_font_color(self):
        """
        obtain proper color for the font
        """
        return None

    def get_ascii(self):
        """
        obtain symbol of this element
        """
        return ''