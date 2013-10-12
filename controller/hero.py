from utilities.generalFunctions import *
from controller.being import *


class HeroSwitch(BeingSwitch):
    """
    controller of hero
    """

    def __init__(self, gear):
        Switch.__init__(self, gear)

        # import key map
        from controller.config.keyMap import hero_
        self.key_map = hero_

        # notify about birth of Hero
        print('a Hero is born')

    def call_action_wait(self):
        print('hero waits')

    def call_action_quit(self):
        print('nothing to do here...')

    def call_action_die(self):
        print('hero have fallen during his quest')

    def call_action_choose_items(self):
        print('choose items to pick up')

    def call_action_move(self, action_result):
        # for successful movement
        if action_result:
            print('hero moved to', self.gear.get_coordinates())
            # try to display items on newly stepped tile
            self.gear.get_current_tile().get_switch().display_items()
        else:
            # this situation is managed by call_action_can_move_to variant
            pass

    def call_action_can_move_to(self, action_result, destination):
        # if movement is not possible
        if not action_result:
            # when there is no destination
            if not destination:
                print('unable to move there')
            # when destination exists, but is not accessible for some reason
            else:
                print('unable to move to', destination.get_coordinates())

    def call_action_collect(self, action_result, collected_items_=[]):
        # when nothing was collected due to lack of items possible to collect
        if not action_result:
            print('nothing to pick up')
        # when attempt to collect some items was made
        else:
            # nothing seemed of interest
            if not collected_items_:
                print('nothing was picked up')
            # some items were chosen to be collected
            else:
                print('picked up', len(collected_items_), 'items')

    def call_action_drop(self, action_result, dropped_items_=[]):
        # when nothing was dropped due to lack of items possible to drop
        if not action_result:
            print('nothing to drop')
        # when attempt to dropped some items was made
        else:
            # no items were chosen to be dropped
            if not dropped_items_:
                print('nothing was dropped')
            # some items were chosen to be dropped
            else:
                print('dropped', len(dropped_items_), 'items')

    def call_show_inventory(self):
        self.gear.get_inventory().get_switch().call_display_items()

    def choose_action(self):
        """
        choose action basing on players input
        """

        action_key = get_key_input()
        # wait for valid command
        while not is_set(self.key_map, action_key):
            print('unknown action')
            action_key = get_key_input()
        # return corresponding method name
        return self.key_map[action_key]
