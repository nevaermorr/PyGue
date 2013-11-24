from utilities.generalFunctions import *
from view.panel import *


class LocationPanel(Panel):
    """
    appearance of location
    """

    def __init__(self, switch):
        Panel.__init__(self, switch, 800, 600)
        self.background_color = pygame.Color(20, 20, 20)