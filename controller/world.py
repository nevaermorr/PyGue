import pygame

from controller.controller import *


class WorldController(Controller):
    """
    main controller for the game
    """

    def __init__(self, model):
        #call parent constructor
        """
        :param model: world that will bo displayed
        """
        Controller.__init__(self, model)

    def callEndGame(self):
        """
        inform the controller about end of the game
        """
        print(self.model.time.getCurrentTime())