from controller.log import *


class Log:
    """
    object responsible for logging necessary information
    """

    def __init__(self):
        # link log with its switch
        self.controller = LogSwitch(self)

    def action_log(self, info):
        """
        information about course of events
        """
        self.controller.call_action_log(info)

    def warning(self, info):
        """
        not allowed action or wrong incoming instruction
        """
        self.controller.call_warning(info)

    def error(self, info):
        """
        error which are not fatal
        """
        self.controller.call_error(info)

    def fatal_error(self, info):
        """
        error which prevents game from further execution
        """
        self.controller.call_fatal_error(info)