
from engine.generalFunctions import *


class Inventory:
    """
    inventory of any being
    """

    def __init__(self, owner):
        #list of items present in the inventory
        self.items_ = []
        #remember owner of this inventory
        self.owner = owner

    def add(self, *items_):
        """
        put something into the inventory
        """
        self.items_.extend(items_)

    def take(self, *items_):
        """
        take something out of the inventory
        """
        items_ = self.get(*items_)
        self.remove(items_)
        return items_

    def get(self, *items_):
        """
        get something from the inventory but don't remove it
        """
        return self.items_
        
    def remove(self):
        """
        take something out of the inventory
        """

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
        self.inventory = Inventory()

    def chooseItems(self, inventory):
        """
        choose items from an inventory
        """
        #by default choose all items
        return inventory.get()

    #TODO copy methods get, add, remove etc from __init__