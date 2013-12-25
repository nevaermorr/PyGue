from utilities.generalFunctions import *
from engine.world import *
import pygame


class MetaWorld(World):
    """
    main machine of the game
    """

    # link to the machine of the world necessary for other views
    # that do not posses direct connection
    link = None

    def __init__(self):
        # inherited constructor
        World.__init__(self)
        # pygame's clock for controlling time
        self.pygame_clock = pygame.time.Clock()
        # create reel for this panel
        self.reel = pygame.display.set_mode(self._determine_resolution())
        # the name of the game
        pygame.display.set_caption('PyGue')
        # position of location panel
        self.location_position = [100, 50]
        # position of clock panel
        self.clock_position = [0, 0]
        # position of log panel
        self.log_position = [150, 0]

        # reference to the world object is stored to the class
        # in order to provide easy access for displaying purposes
        MetaWorld.link = self

    def _determine_resolution(self):
        """
        determine resolution of the main window
        """
        # for now start with static resolution
        return 1000, 600

    def compose_reel(self):
        # inherited routines
        MetaGear.compose_reel(self)
        # map occupies main part of the game interface
        self.reel.blit(self.current_location.get_reel(), self.location_position)
        # display the clock
        self.reel.blit(self.clock.get_reel(), self.clock_position)
        # display the log
        self.reel.blit(self.log.get_reel(), self.log_position)

    def display(self):
        """
        present everything on the screen
        """
        # compose all the elements that are to be displayed
        self.compose_reel()
        # display the whole world
        pygame.display.update()

    # methods operating on the engine

    @staticmethod
    def end_game():
        World.game_over = True

    def clean_up(self):
        # quit pygame
        pygame.quit()