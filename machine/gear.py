from utilities.generalFunctions import *
import pygame
from engine.gear import *
from machine.panel import *


class MetaGear(Gear, Panel):
    """
    every element of the machine
    """

    def __init__(self, width=25, height=25):
        # inherited constructors
        Gear.__init__(self)
        Panel.__init__(self, width, height)

    def _get_key(self):
        """
        obtain pressed key
        """
        # ignore existing cue
        pygame.event.clear()
        # pay attention only to keys and quits
        pygame.event.set_allowed(None)
        pygame.event.set_allowed((pygame.KEYDOWN, pygame.QUIT))
        # read the actual key
        return pygame.event.wait()