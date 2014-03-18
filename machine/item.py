from utilities.general_functions import *
import pygame
from engine.item import *
from machine.symbolic_panel import SymbolicPanel


class MetaItem(Item, SymbolicPanel):
    """
    complement of entity
    """

    def __init__(self):
        # inherited constructors
        Item.__init__(self)
        #TODO extract default symbols to external file
        SymbolicPanel.__init__(self, symbol='&')