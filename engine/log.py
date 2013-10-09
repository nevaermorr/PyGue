from controller.log import *


class Log:
    """
    object responsible for logging necessary information
    """

    def __init__(self):
        #link log with its controller
        self.controller = LogController(self)

    def actionLog(self, info):
        """
        information about course of events
        """
        self.controller.callActionLog(info)

    def warning(self, info):
        """
        not allowed action or wrong incoming instruction
        """
        self.controller.callWarning(info)

    def error(self, info):
        """
        error which are not fatal
        """
        self.controller.callError(info)

    def fatalError(self, info):
        """
        error which prevents game from further execution
        """
        self.controller.callFatalError(info)