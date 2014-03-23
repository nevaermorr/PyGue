from utilities.general_functions import *
import pygame
from engine.item import *
from machine.symbolic_panel import SymbolicPanel


class MetaItem(Item, SymbolicPanel):
    """
    complement of entity
    """
    def __init__(self, location, x, y):
        # inherited constructors
        Item.__init__(self, location, x, y)
        SymbolicPanel.__init__(
            self,
            font_size=25,
        )
        #TODO extract default symbols to external file
        self.symbol = '&'