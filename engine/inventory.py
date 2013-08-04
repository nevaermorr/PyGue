from engine.generalFunctions import *
from engine.displayableList import *


class Inventory(DisplayableList):
    """
    set of items connected with some entity or place
    """

    def __init__(self, owner):
        #list of items present in the inventory
        self.items_ = []
        #items serve as the basis for displayableList
        DisplayableList.__init__(self, self.items_)
        #remember owner of this inventory
        self.owner = owner

    def add(self, *items_):
        """
        put something into the inventory
        """
        self.items_.extend(items_)

    def remove(self, *items_):
        """
        remove something from the inventory
        """
        #delete items from inventory through list comprehension
        self.items_ = [item for item in self.items_ if not item in items_]

    def chooseAll(self, condition=False):
        """
        get from the inventory all items that meet certain condition
        """
        #by default, get all the items
        if not condition:
            return self.items_

    def isEmpty(self):
        """
        check if inventory is empty
        """
        return not bool(self.items_)


class InventoryInterface:
    """
    interface for all classes containing some inventory
    """

    def __init__(self):
        #inventory is obligatory
        self.inventory = Inventory(self)

    def accessInventory(self):
        """
        grant access to the inventory
        """
        return self.inventory

    def getItemsFrom(self, inventory):
        """
        choose and obtain items from an inventory
        """
        #by default choose all possible items
        items_ = inventory.chooseAll()
        #remove all the items from original inventory (in order to avoid duplication)
        inventory.remove(*items_)
        return items_

    def addItems(self, *items_):
        """
        shortcut for adding items to inventory
        """
        self.inventory.add(*items_)