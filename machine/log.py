from utilities.generalFunctions import *
import pygame
from engine.log import *


class MetaLog(Log):
    """
    appearance of log
    """

    def __init__(self):
        Log.__init__(self)

        self.action_log_ = []
        self.message_log_ = []
        self.warning_log_ = []
        self.error_log_ = []
        self.fatal_error_log = []

        # visuals
        self.font_color = pygame.Color(255, 255, 255)
        self.font = pygame.font.Font('utilities/fonts/rough_typewriter.otf', 30)

    def action(self, *info):
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