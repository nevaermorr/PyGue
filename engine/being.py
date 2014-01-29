from utilities.generalFunctions import *
from machine.entity import *
from machine.inventory import *


class Being(MetaEntity, MetaInventoryInterface):
    """
    entity capable of taking actions
    """

    def __init__(self, location, x, y, species):
        """
        create being
        :param location: location where the being is placed
        :param x: horizontal coordinate
        :param y: vertical coordinate
        :param species: species of this being
        """
        # inherited constructor
        MetaEntity.__init__(self, location, x, y)
        #provide the being with space for its belongings
        MetaInventoryInterface.__init__(self)
        # initialize species-dependent features
        self.species = None
        # time costs of all actions
        self.action_time_costs_ = {}
        # time needed before being can act
        self.cool_down = 0
        # how far can this being see
        self.range_of_view_ = {
            # full details
            'visible': 0,
            # silhouettes only
            'shadow': 0
        }
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
        # how far can this being see
        self.range_of_view_ = species_dependency.range_of_view_

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
            # find action time cost
            if not is_set(self.action_time_costs_, action_name):
                time_cost = 0
            else:
                time_cost = self.action_time_costs_[action_name]
            # set cool-down to time cost of chosen action
            self.cool_down += time_cost
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

    def get_square_range_of_view(self):
        """
        obtain squared range of view
        """
        return {index: s_range ** 2 for index, s_range in self.range_of_view_.items()}

    def in_line_of_sight(self, target):
        """
        examine if given point is in line of sight of the being
        :param target: point as object of class Spatial
        """
        # start with empty previous step
        previous_step_ = []
        # check each step of the route to see if it is not blocked
        for step_ in self.get_beam_route_to(target.get_x(), target.get_y()):
            transparent_ = [
                # coordinates
                tile_
                # of each tile in a step
                for tile_ in step_
                # which is transparent
                if self.location.get_tile_by_coordinates(*tile_).is_transparent()
            ]
            # if all tiles belonging to this step are opaque, the line of sight is blocked
            if not transparent_:
                return False

            # if this is beginning of the route,
            # there is no possibility of discontinuity for the transparent tiles
            if not previous_step_:
                # note the current step
                previous_step_ = transparent_
                continue

            # otherwise check if any of the transparent tiles
            # is connected to any of the previous ones (so the view is not blocked)
            if not any([self.location.get_tile_by_coordinates(*point_).neighbours_with(*previous_point_)
                       for point_ in transparent_ for previous_point_ in previous_step_]):
                return False

            # note the current step
            previous_step_ = transparent_

        # if nothing was in the way - target is in line of sight
        return True