from utilities.general_functions import *
from machine.entity import *


class Item(MetaEntity):
    """
    usable item
    """

    def __init__(self, location, x, y):
        """
        creation of item
        """
        # inherited state
        MetaEntity.__init__(self, location, x, y)
        # inform tile about presence of new item
        self.get_current_tile().add_items(self)