from utilities.generalFunctions import *
import pygame
from engine.gear import *
from machine.panel import *


class MetaGear(Gear, Panel):
    """
    every element of the machine
    """

    def __init__(self, width=25, height=25):
        """
        creation of the gear
        """
        # inherited constructors
        Gear.__init__(self)
        Panel.__init__(self, width, height)

    def _get_key(self, unicode=False):
        """
        obtain pressed key
        :param unicode: flag for choosing between bare unicode or full pygame key object
        """
        # make sure that visible situation is up to date
        self.force_display()
        # clear log buffer once it is displayed
        self.log.clear_buffer()

        # ignore existing cue
        pygame.event.clear()
        # pay attention only to keys and quits
        pygame.event.set_allowed(None)
        pygame.event.set_allowed((pygame.KEYDOWN, pygame.QUIT))
        # read the actual key
        key = pygame.event.wait()

        # if bare unicode is desired
        if unicode:
            return key.unicode

        # if full pygame key object is preferred
        else:
            return key

    def _get_direction(self, vector=True):
        """
        obtain direction from directional keys
        :param vector: flag for choosing between vector and literal key
        """
        key = self._get_key(True)

        # if literal
        if not vector:
            if key in ['1', '2', '3', '4', '6', '7', '8', '9']:
                return key

        # if vector is preferred
        elif key == '1':
            return [-1, 1]
        elif key == '2':
            return [0, 1]
        elif key == '3':
            return [1, 1]
        elif key == '4':
            return [-1, 0]
        elif key == '6':
            return [1, 0]
        elif key == '7':
            return [-1, -1]
        elif key == '8':
            return [0, -1]
        elif key == '9':
            return [1, -1]

        # if none of the above - read keys until proper is pressed
        return self._get_direction(vector)