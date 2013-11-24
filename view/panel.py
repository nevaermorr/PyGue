from utilities.generalFunctions import *
import pygame


class Panel:
    """
    every element of the view
    """

    def __init__(self, switch, height=1, width=1):
        # switch corresponding to this panel
        self.switch = switch
        # set resolution of this panel
        self.resolution = [height, width]
        # personal reel exclusive for this element
        self.reel = None
        # default font
        self.font = pygame.font.SysFont('ubuntumono.ttf', 24)
        # default font color
        self.font_color = pygame.Color(255, 255, 255)
        # default background color
        self.background_color = pygame.Color(0, 0, 0)

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
        # to be implemented by inheriting panel
        # TODO automatically clear the background
        pass