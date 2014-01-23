from utilities.generalFunctions import *
import pygame


class Panel:
    """
    common class for elements with visualisation on the screen
    """

    def __init__(
            self, width, height,
            background_color=pygame.Color(0, 0, 0),
            font_path='utilities/fonts/veteran_typewriter.ttf',
            font_color=pygame.Color(255, 255, 255),
            font_size=45
    ):
        """
        creation of the panel
        """
        # initialize visual options

        # resolution of this panel
        self.width = 0
        self.height = 0
        # personal reel exclusive for this element
        self.reel = None
        # storage for additional temporal reels for outer overlays
        self.overlay_ = []
        # path to the font file
        self.font_path = None
        # size of the font
        self.font_size = None
        # font object
        self.font = None
        # color of text
        self.font_color = None
        # color of the background;
        # None for transparent background
        self.background_color = None

        # set visual options
        self.set_panel_options(
            width, height, font_path, font_size, font_color, background_color
        )

    def set_panel_options(
            self,
            width=None,
            height=None,
            font_path=None,
            font_size=None,
            font_color=None,
            # little workaround - "None" stands for transparent background
            # thus cannot be used as default
            background_color='x',
    ):
        """
        set visual options for the panel
        """

        if width:
            self.width = width
        if height:
            self.height = height
        # re-form the reel if necessary
        if width or height:
            self.reel = pygame.Surface((width, height), pygame.SRCALPHA, 32)

        if font_path:
            self.font_path = font_path
        if font_size:
            self.font_size = font_size
        # re-form the font object if necessary
        if font_path or font_size:
            self.font = pygame.font.Font(font_path, font_size)

        # default font color
        if font_color:
            self.font_color = font_color
        # default background color
        if background_color != 'x':
            self.background_color = background_color

    def force_display(self):
        """
        display current state of the game on the screen
        """
        from machine.world import MetaWorld

        MetaWorld.link.display()

    def get_reel(self, recompose=True):
        """
        obtain element in ready-to-display form
        :parameter recompose: should the reel be recomposed before returning?
        """
        # perform re-composition if necessary
        if not self.reel or recompose:
            self.compose_reel()
            # add overlay if necessary
            self.overlay_reel()
        # one way or another - return the reel
        return self.reel

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # to be implemented by inheriting element
        # by default clear the whole reel
        if self.reel:
            # if the element has opaque background
            if self.background_color:
                self.reel.fill(self.background_color)
            # if the element has transparent background
            else:
                self.reel.fill(pygame.Color(0, 0, 0, 0))

    def overlay_reel(self):
        for layer in self.overlay_:
            self.reel.blit(layer, [0, 0])

    def add_overlay(self, reel):
        """
        add some temporal elements that are to be additionally displayed
        :param reel: additional reel to combine with the proper one
        """
        self.overlay_.append(reel)

    def remove_overlay(self, reel):
        """
        remove some temporal elements that are no longer needed to be additionally displayed
        :param reel: additional reel to combine with the proper one
        """
        self.overlay_.remove(reel)