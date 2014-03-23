from utilities.general_functions import *
import pygame
from engine.inventory import *
from machine.symbolic_panel import *


class MetaInventory(Inventory, SymbolicPanel):
    """
    complement of inventory
    """

    def __init__(self, owner):
        # inherited routines
        Inventory.__init__(self, owner)
        SymbolicPanel.__init__(self)

    def compose_reel(self):

        # empty reel for empty inventory
        if self.is_empty():
            SymbolicPanel.compose_reel()
            return False

        # for now display only the first item
        self.reel = self.items_[0].get_reel()
        return True

        # # font object for symbol
        # symbol = self.font.render(self.get_symbol(), True, pygame.Color(200, 200, 200))

        # in case of single item
        # if self.count_items() == 1:
        #     # print centered
        #     self.reel.blit(
        #         symbol,
        #         ((self.pixel_width - symbol.get_width()) / 2,
        #          (self.pixel_height - symbol.get_height()) / 2)
        #     )
        #
        # elif self.count_items() == 2:
        #     pass
        #
        # # in case of 3 or more items
        # elif self.count_items() > 2:
        #     # print centered
        #     self.reel.blit(
        #         symbol,
        #         ((self.pixel_width - symbol.get_width()) / 2,
        #          (self.pixel_height - symbol.get_height()) / 2)
        #     )


class MetaInventoryInterface(InventoryInterface):
    """
    complement of element containing an inventory
    """