from utilities.generalFunctions import *
import pygame


class Panel:
    """
    common class for elements with visualisation on the screen
    """

    def __init__(self, width, height):

        # set resolution of this element
        self.resolution = [width, height]
        # personal reel exclusive for this element
        self.reel = pygame.Surface((width, height))
        # default font
        #self.font = pygame.font.SysFont('ubuntumono.ttf', 48)
        #self.font = pygame.font.Font('utilities/fonts/rough_typewriter.otf', 30)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 45)
        # default font color
        self.font_color = pygame.Color(255, 255, 255)
        # default background color
        self.background_color = pygame.Color(0, 0, 0)
        # ascii symbol of the gear
        self.ascii = ''

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