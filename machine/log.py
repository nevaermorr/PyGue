from utilities.general_functions import *
import pygame
from engine.log import *
from machine.panel import *


class MetaLog(Log, Panel):
    """
    complement of log
    """

    def __init__(self):
        """
        creation of the log
        """
        # inherited constructors
        Log.__init__(self)
        Panel.__init__(self, 600, 50)

        # logs - for storing all the information
        self.action_log_ = []
        self.message_log_ = []
        self.warning_log_ = []
        self.error_log_ = []
        self.fatal_error_log_ = []

        # buffers - for temporarily storing information that has not yet been displayed
        self.action_buffer_ = []
        self.message_buffer_ = []
        self.warning_buffer_ = []
        self.error_buffer_ = []
        self.fatal_error_buffer_ = []

        # visuals from panel
        self.font_color = pygame.Color(255, 255, 255)
        self.font = pygame.font.Font('utilities/fonts/linowrite.ttf', 20)
        # additional visuals
        self.font_color_error = pygame.Color(255, 10, 10)

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
        # add the information to the message buffer
        self.message_buffer_.append(*info)

    def warning(self, *info):
        """
        action not allowed or wrong incoming instruction
        """
        # add the information to the warning buffer
        self.warning_buffer_.append(*info)

    def error(self, *info):
        """
        error which is not fatal
        """
        # for now print it to the console
        print(*info)

    def fatal_error(self, *info):
        """
        error which prevents game from further execution
        """
        # for now print ot to the console
        print(*info)

    def compose_reel(self):
        """
        combine all the elements that are to be displayed on this layer
        """
        # inherited routine
        Panel.compose_reel(self)

        # compose string with information from buffers
        info = ''
        if self.warning_buffer_:
            info += '\n'.join(self.warning_buffer_)
        if self.message_buffer_:
            info += '\n'.join(self.message_buffer_)
        # take information from the buffer and clear it afterwards
        text = self.font.render(info, True, self.font_color)

        self.reel.blit(text, [0, 0])

    def clear_buffer(self):
        """
        delete all information from all buffers
        """
        # TODO move all buffered information to the log
        # clear the buffer
        self.action_buffer_ = []
        self.message_buffer_ = []
        self.warning_buffer_ = []
        self.error_buffer_ = []
        self.fatal_error_buffer_ = []