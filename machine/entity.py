from utilities.generalFunctions import *
import pygame
from engine.entity import *
from machine.symbolicPanel import *


class MetaEntity(Entity, SymbolicPanel):
    """
    complement of entity
    """

    def __init__(self, *parameters):
        """
        creation of entity
        """
        # inherited constructors
        Entity.__init__(self, *parameters)
        SymbolicPanel.__init__(self, self.width, self.height)

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # inherited routine - SymbolicPanel version over the one inherited from Entity
        SymbolicPanel.compose_reel(self)