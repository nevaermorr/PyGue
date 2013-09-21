from generalFunctions import *
from view.log import *


class Log:
    """
    object responsible for logging necessary information
    """

    def __init__(self):
        #link log with its view
        self.view = LogView(self)

    def actionLog(self, info):
        """
        information about course of events
        """

    def warning(self, info):
        """
        not allowed action or wrong incoming instruction
        """

    def error(self, info):
        """
        error which are not fatal
        """

    def fatalError(self, info):
        """
        error which prevents game from further execution
        """