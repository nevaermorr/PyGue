from utilities.generalFunctions import *
from machine.gear import *
from machine.clock import *


class World(MetaGear):
    """
    the game universe
    """
    # boolean flag ending the game
    game_over = False

    def __init__(self):
        """
        creation of the world!
        """
        MetaGear.__init__(self)
        # initialize locations
        self.locations_ = None
        self.current_location = None
        # start the great clock
        self.clock = MetaClock()
        # initialize some environment
        self.create_environment()

    def run(self):
        """
        main loop running the game
        """
        while not World.game_over:
            # time flies
            self.clock.pass_time()
            # give a chance to act for everything that is eligible for acting
            for being in self.current_location.get_beings():
                being.act()
                # no point in letting anyone act if the game is over
                if World.game_over:
                    break

        #once the game is over make sure to clean up after it
        self.clean_up()

    def clean_up(self):
        """
        clean up everything before exiting the program
        """
        pass

    @staticmethod
    def end_game():
        """
        manage everything that needs to be done once the game comes to its end
        """
        World.game_over = True

    def create_environment(self):
        """
        create some environment for testing purposes
        """
        from data.environment.testEnvironment import initEnvironment

        # a single map will do for now
        self.locations_ = initEnvironment()
        # pointer to current location
        self.set_current_location(self.locations_[0])

    def set_current_location(self, location):
        """
        change current location to another
        """
        self.current_location = location

    def get_clock(self):
        """
        access the clock
        """
        return self.clock