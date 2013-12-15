from utilities.generalFunctions import *
import pygame
from engine.log import *


class MetaLog(Log):
    """
    appearance of log
    """

    def action_log(self, *info):
        """
        information about course of events
        """
        # for the time being - do not bother;
        # the purpose of this is for now to keep possible action log calls in the code
        pass

    def message(self, *info):
        """
        information to be displayed to the player
        """
        print(*info)

    def warning(self, *info):
        """
        action not allowed or wrong incoming instruction
        """
        print(*info)

    def error(self, *info):
        """
        error which is not fatal
        """
        print(*info)

    def fatal_error(self, *info):
        """
        error which prevents game from further execution
        """
        print(*info)