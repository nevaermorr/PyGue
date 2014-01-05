from utilities.generalFunctions import *
from machine.entity import *
from machine.inventory import *


class Being(MetaEntity, MetaInventoryInterface):
    """
    entity capable of taking actions
    """

    def __init__(self, location, coordinates_, species):
        """
        create being
        :param location: location where the being is placed
        :param coordinates_: coordinates depicting the position of being in given location
        :param species: species of this being
        """
        # inherited constructor
        MetaEntity.__init__(self, location, coordinates_)
        #provide the being with space for its belongings
        MetaInventoryInterface.__init__(self)
        # initialize species-dependent features
        self.species = None
        self.action_time_costs_ = {}
        self.cool_down = 0
        # load species-dependent features
        self.load_species_dependencies(species)
        # announce that a new being has arrived
        location.check_in(self)

    def load_species_dependencies(self, species):
        """
        load all species-dependent information
        :param species: species of this being
        """
        # remember species, just in case
        self.species = species
        # import proper file
        module = __import__('data.being.species.' + species, fromlist=[])
        species_dependency = getattr(module.being.species, species)

        # time costs of different actions
        self.action_time_costs_ = species_dependency.timeCosts_
        # time needed between creation and first action
        self.cool_down = species_dependency.summoningSickness

    def act(self):
        """
        combination of all elements required to act
        """
        self.decrease_cool_down()
        # if being is ready for action
        if self.is_ready_to_act():
            # choose and try to perform some action until performed successfully
            while not self.perform_action(*self.choose_action()):
                pass

    def choose_action(self):
        """
        choose what action will the being undertake
        """
        # wait by default
        return ['wait']

    def decrease_cool_down(self):
        """
        decrease cool-down every time quantum
        """
        if self.cool_down > 0:
            self.cool_down -= 1

    def is_ready_to_act(self):
        """
        check if the state of the being allows it to act
        """
        if self.cool_down == 0:
            return True

    def perform_action(self, action_name, *action_parameters_):
        """
        call proper methods resolving certain actions
        :param action_name: name of desired action
        :param action_parameters_: list of parameters for action
        """
        # perform desired action
        action_result = getattr(self, action_name)(*action_parameters_)
        # if action performed successfully
        if action_result:
            # set cool-down to time cost of chosen action
            self.cool_down += self.action_time_costs_[action_name]
        # report success or failure of action
        return action_result

    def die(self):
        """
        trigger all death effects
        """
        # this being is no more
        self.location.check_out(self)

    def wait(self):
        """
        pass one turn
        """
        # wait is always successful
        return True

    def collect(self):
        """
        collect some items
        """
        # add items chosen from current tile's inventory
        collected_items_ = self.get_items_from(self.get_current_tile().get_inventory())
        # if there is anything to pick up
        if collected_items_:
            self.add_items(*collected_items_)
            # collected successfully
            return True
        else:
            # failed to collect
            return False

    def drop(self):
        """
        drop some items
        """
        # choose items to drop (as for now - all)
        dropped_items = self.get_items_from()
        self.get_current_tile().add_items(*dropped_items)
        return True

    def manipulate_door(self, door):
        """
        open some door
        """
        # if door is open - close it
        door.manipulate()