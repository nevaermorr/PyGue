from utilities.generalFunctions import *
from view.panel import *
from view.world import *


class HeroPanel(Panel):
    """
    appearance of hero
    """

    def call_is_ready_to_act(self):
        """
        proceed with necessary actions when the hero is ready to act
        """
        WorldPanel.link.display()
