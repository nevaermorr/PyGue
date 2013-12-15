from utilities.generalFunctions import *
from machine.being import *


class Hero(MetaBeing):
    """
    player character
    """

    def perform_action(self, action_name, *action_parameters_):
        result = Being.perform_action(self, action_name, *action_parameters_)
        # return original result
        return result

    def load_species_dependencies(self, species):
        Being.load_species_dependencies(self, species)
        # only heroes can quit
        self.action_time_costs_['quit'] = 0

    def quit(self):
        """
        quit the game
        """
        from machine.world import MetaWorld

        # notify the world about pointlessness of its existence
        MetaWorld.end_game()
        # successful quit
        return True

    def die(self):
        """
        what happens when hero dies
        """
        MetaBeing.die(self)
        # leave it all behind
        self.quit()

    def get_items_from(self, inventory=False):
        # if no outer inventory is provided, assume own inventory is needed
        if not inventory:
            inventory = self.inventory
        # get items normally
        items_ = MetaBeing.get_items_from(self, inventory)
        # return items in question
        return items_

    def collect(self):
        #check if there is anything to take
        if self.get_current_tile().get_inventory().is_empty():
            return False
        #if tile is not empty, proceed normally
        return MetaBeing.collect(self)

    def drop(self):
        #check if there is anything to drop
        if self.inventory.is_empty():
            return False
        #if tile is not empty, proceed normally
        return MetaBeing.drop(self)

    def show_inventory(self):
        """
        display owned items
        """
        return True