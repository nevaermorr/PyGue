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

        # ascii symbol for the construction
        self.ascii = None
        # color of the construction
        self.font_color = None