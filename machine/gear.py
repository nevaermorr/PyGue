from utilities.generalFunctions import *
import pygame
from engine.gear import *


class MetaGear(Gear):
    """
    every element of the machine
    """

    def __init__(self, height=25, width=25):
        # set resolution of this element
        self.resolution = [height, width]
        # personal reel exclusive for this element
        self.reel = pygame.Surface((width, height))
        # default font
        self.font = pygame.font.SysFont('ubuntumono.ttf', 48)
        # default font color
        self.font_color = pygame.Color(255, 255, 255)
        # default background color
        self.background_color = pygame.Color(0, 0, 0)
        # ascii symbol of the gear
        self.ascii = ''

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

    def force_display(self):

        from machine.world import MetaWorld
        MetaWorld.link.display()

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
        # by default clear the whole reel
        if self.reel:
            self.reel.fill(self.background_color)