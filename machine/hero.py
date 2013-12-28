from utilities.generalFunctions import *
import pygame
from engine.hero import *


class MetaHero(Hero):
    """
    appearance of hero
    """

    def __init__(self, location, coordinates_, species):

        Hero.__init__(self, location, coordinates_, species)

        # import key map
        from config.keyMap import hero_
        self.key_map = hero_

        # visuals
        self.ascii = '@'
        self.set_panel_options(
            background_color=None,
            font_color=pygame.Color(20, 255, 20),
        )
        # font temporarily defined directly
        #self.font = pygame.font.Font('utilities/fonts/linowrite.ttf', 30)
        self.font = pygame.font.Font('utilities/fonts/veteran_typewriter.ttf', 25)

        self.log.message('A hero is born')

    def choose_action(self):
        # repeat reading keyboard input until an action is undertaken
        while 1:
            # make sure that visible situation is up to date
            self.force_display()
            # clear log buffer once it is displayed
            self.log.clear_buffer()
            key = self._get_key()
            # for closing game in an old fashioned manner - clicking X or alt+F4
            if key.type == pygame.QUIT:
                return ['quit']

            # for actions mapped to the keys
            if is_set(self.key_map, key.unicode):
                return self.key_map[key.unicode]

            # otherwise report invalid action unless it is due to some functional key
            if key.unicode != '':
                self.log.warning('unknown action \'' + key.unicode + '\'')

    def wait(self):
        # original action
        result = Hero.wait(self)
        self.log.message('Hero waits')
        # return the original result
        return result

    def quit(self):
        # original action
        result = Hero.quit(self)
        self.log.message('Nothing to do here...')
        # return the original result
        return result

    def die(self):
        # original action
        result = Hero.die(self)
        self.log.message('Hero have fallen during his quest')
        # return the original result
        return result

    def move(self, direction_):
        # original action
        result = Hero.move(self, direction_)
        # for successful movement
        if result:
            self.log.action('Hero moved to', self.coordinates_)
        # return the original result
        return result

    def can_move_to(self, coordinates_):
        # original action
        result = Hero.can_move_to(self, coordinates_)
        # if movement is not possible
        if not result:
            self.log.warning('unable to move there')
        # return the original result
        return result

    def compose_reel(self):
        SymbolicPanel.compose_reel(self)

    def get_ascii(self):
        return self.ascii