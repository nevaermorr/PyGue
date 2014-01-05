from utilities.generalFunctions import *
from machine.construction import *


class Door(MetaConstruction):
    """
    a section of wall on the map
    """

    def __init__(self, opened=False):
        # inherited constructor
        MetaConstruction.__init__(self, 'door')
        # is it open?
        self.opened = opened
        # is it locked?
        self.locked = False

    def is_passable(self):
        """
        is it possible to pass through this construction?
        """
        # doors are passable if open
        return self.opened

    def is_transparent(self):
        """
        is it possible to see through door
        """
        # doors are transparent if open
        return self.opened

    def manipulate(self):
        """
        change the open/closed state of the door
        """
        # just flip it
        self.opened = not self.opened