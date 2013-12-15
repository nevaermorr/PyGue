from utilities.generalFunctions import *
from machine.entity import *


class Item(MetaEntity):
    """
    usable item
    """

    def __init__(self, location, coordinates_):
        # inherited state
        MetaEntity.__init__(self, location, coordinates_)
        # inform tile about presence of new item
        self.get_current_tile().add_items(self)