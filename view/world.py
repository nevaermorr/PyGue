from generalFunctions import *
from view.view import *


class WorldView(View):
    """
    main view for the game
    """

    def __init__(self, model):
        #call parent constructor
        """
        :param model: world that will bo displayed
        """
        View.__init__(self, model)

    def callEndGame(self):
        """
        inform the view about end of the game
        """
        print(self.model.time.getCurrentTime())