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

    def open(self):
        """
        open the door
        """
        self.opened = True

    def close(self):
        """
        close the door
        """
        self.opened = False

    def manipulate(self):
        """
        change the open/closed state of the door
        """
        # just flip it
        self.opened = not self.opened