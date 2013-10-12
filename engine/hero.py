from utilities.generalFunctions import *
from engine.being import *
from controller.hero import *


class Hero(Being):
    """
    player character
    """

    def __init__(self, location, coordinates_, species):

        Being.__init__(self, location, coordinates_, species)
        # assign the switch
        self.switch = HeroSwitch(self)

    @doc_inherit
    def perform_action(self, action_name, *action_parameters_):
        result = Being.perform_action(self, action_name, *action_parameters_)
        # return original result
        return result

    @doc_inherit
    def load_species_dependencies(self, species):
        Being.load_species_dependencies(self, species)
        # only heroes can quit
        self.action_tme_costs_['quit'] = 0

    def quit(self):
        """
        quit the game
        """
        from engine.world import World

        # notify the world about pointlessness of its existence
        World.game_over = True
        # notify the switch about the situation
        self.switch.call_action_quit()
        # successful quit
        return True

    def die(self):
        """
        what happens when hero dies
        """
        Being.die(self)
        # leave it all behind
        self.quit()

    def wait(self):
        result = Being.wait(self)
        self.switch.call_action_wait()
        # return the original result
        return result

    def move(self, direction_):
        # move like other beings
        # if movement failed
        if not Being.move(self, direction_):
            # report failure of movement
            return False
        # if movement succeeded
        else:
            # notify the switch
            self.switch.call_action_move(True)
            # report success of movement
            return True

    @doc_inherit
    def add_items(self, *items_):
        # add items normally
        Being.add_items(self, *items_)

    @doc_inherit
    def get_items_from(self, inventory=False):
        # if no outer inventory is provided, assume own inventory is needed
        if not inventory:
            inventory = self.inventory
        # get items normally
        items_ = Being.get_items_from(self, inventory)
        # return items in question
        return items_

    @doc_inherit
    def collect(self):
        #check if there is anything to take
        if self.get_current_tile().get_inventory().is_empty():
            #notify the switch
            self.switch.call_action_collect(False)
            return False
        #if tile is not empty, proceed normally
        return Being.collect(self)

    @doc_inherit
    def drop(self):
        #check if there is anything to drop
        if self.inventory.is_empty():
            self.switch.call_action_drop(False)
            return False
        #if tile is not empty, proceed normally
        return Being.drop(self)

    def show_inventory(self):
        """
        display owned items
        """
        self.switch.call_show_inventory()
        return True