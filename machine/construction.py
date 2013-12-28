from utilities.generalFunctions import *
import pygame
from engine.construction import *


class MetaConstruction(Construction):
    """
    appearance of the construction
    """

    def __init__(self):
        # inherited constructor
        Construction.__init__(self)

    def get_font_color(self):
        return None

    def get_ascii(self):
        return ''