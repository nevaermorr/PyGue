from utilities.generalFunctions import *
from machine.gear import *


class MetaLocation(MetaGear):
    """
    appearance of location
    """

    def __init__(self, switch):
        MetaGear.__init__(self, switch, 800, 600)
        self.background_color = pygame.Color(20, 20, 20)