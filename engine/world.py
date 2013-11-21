from engine.gear import *
from engine.clock import *
from controller.world import *


class World(Gear):
    """
    the game universe
    """
    # boolean flag ending the game
    game_over = False

    def __init__(self):
        """
        creation of the world!
        """

        Gear.__init__(self)
        # initialize locations
        self.locations_ = None
        self.current_location = None
        # start the great clock
        self.clock = Clock()
        # link world with its switch
        self.switch = WorldSwitch(self)
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
        # game over here
        else:
            self.end_game()

    def end_game(self):
        """
        manage everything that needs to be done once the game come to its end
        """
        # notify the switch about end of the game
        self.switch.call_end_game()

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
        # inform the switch
        self.switch.call_set_current_location(location)

    def get_clock(self):
        """
        access the clock
        """
        return self.clock