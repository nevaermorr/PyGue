from utilities.generalFunctions import *
import pygame
from engine.gear import *


class MetaGear(Gear):
    """
    every element of the machine
    """

    def __init__(self, height=1, width=1):
        # set resolution of this element
        self.resolution = [height, width]
        # personal reel exclusive for this element
        self.reel = None
        # default font
        self.font = pygame.font.SysFont('ubuntumono.ttf', 24)
        # default font color
        self.font_color = pygame.Color(255, 255, 255)
        # default background color
        self.background_color = pygame.Color(0, 0, 0)

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

    def get_reel(self, recompose=True):
        """
        obtain element in ready-to-display form
        :parameter recompose: should the reel be recomposed before returning?
        """
        # perform re-composition if necessary
        if recompose:
            self.compose_reel()
        # one way or another - return the reel
        return self.reel

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # to be implemented by inheriting element
        # TODO automatically clear the background
        pass