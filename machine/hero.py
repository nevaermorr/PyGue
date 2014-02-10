from utilities.general_functions import *
import pygame
from engine.hero import *


class MetaHero(Hero):
    """
    complement of hero
    """
    # resources necessary for drawing targeting
    from machine.symbolic_panel import SymbolicPanel
    from machine.tile import MetaTile
    crosshair_shadow = SymbolicPanel(
        MetaTile.width, MetaTile.height,
        symbol='x',
        font_size=20,
        background_color=pygame.Color(0, 0, 0, 0)
    )
    crosshair = SymbolicPanel(
        MetaTile.width, MetaTile.height,
        symbol='x',
        font_size=30,
        background_color=pygame.Color(0, 0, 0, 0)
    )

    def __init__(self, *parameters):
        """
        creation of the hero
        """
        # inherited constructors
        Hero.__init__(self, *parameters)

        # import key map
        from config.key_map import hero_
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
        """
        choose what action will the being undertake
        """
        # repeat reading keyboard input until an action is undertaken
        while 1:
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
        """
        pass one turn
        """
        # original action
        result = Hero.wait(self)
        self.log.message('Hero waits')
        # return the original result
        return result

    def quit(self):
        """
        quit the game
        """
        # original action
        result = Hero.quit(self)
        self.log.message('Nothing to do here...')
        # return the original result
        return result

    def die(self):
        """
        what happens when hero dies
        """
        # original action
        result = Hero.die(self)
        self.log.message('Hero have fallen during his quest')
        # return the original result
        return result

    def move(self, direction_):
        """
        what happens when some force moves the entity
        :param direction_: direction of the movement given as [x,y] vector
        """
        # original action
        result = Hero.move(self, direction_)
        # for successful movement
        if result:
            self.log.action('Hero moved to', self.x, self.y)
        # return the original result
        return result

    def can_move_to(self, x, y):
        """
        check if certain position in the location is accessible for this entity
        :param x: horizontal coordinate of desired position
        :param y: vertical coordinate of desired position
        """
        # original action
        result = Hero.can_move_to(self, x, y)
        # if movement is not possible
        if not result:
            self.log.warning('unable to move there')
        # return the original result
        return result

    def get_symbol(self):
        """
        obtain symbol of this element
        """
        return self.ascii

    def manipulate_door(self, door=None):
        # if the door is unspecified - ask
        if not door:
            # if the door are not specified, ask for it
            self.log.message('Which direction?')
            direction_ = self._get_direction()

            target_tile = self.location.get_tile_by_coordinates(
                self.get_x() + direction_[0],
                self.get_y() + direction_[1]
            )
            if target_tile:
                # if target tile has some construction on it
                construction = target_tile.get_construction()
                # if it is a door
                if construction and construction.get_sort() == 'door':
                    door = construction

        # if the door was still not specified
        if not door:
            self.log.warning('There is no door there')
            # opening door failed
            return False
        # in the end, open the door
        return Hero.manipulate_door(self, door)

    def aim(self):
        """
        choose target by freely moving the crosshair
        """
        self.log.message('Choose target')
        # current position of crosshair
        target_ = [self.get_x(), self.get_y()]

        direction_ = self._get_direction(confirm=True)

        while direction_:
            # once the target is confirmed retrieve its coordinates
            if direction_ is True:
                return target_
            # aiming is being aborted
            elif direction_ is False:
                return False
            # if proper direction was chosen, change position of the crosshair
            else:

                target_[0] += direction_[0]
                target_[1] += direction_[1]

            self.draw_targeting_line(target_)

            self.log.message('Choose target')
            direction_ = self._get_direction(confirm=True)

            self.erase_targeting_line(target_)

        # targeting aborted
        return False

    def draw_targeting_line(self, target_):
        """
        draw marks on tiles that are in the line of sight to the target
        :param target_: coordinates of the target
        """
        # acquire target tile
        target_tile = self.location.get_tile_by_coordinates(*target_)
        # mark the target
        if target_tile:
            target_tile.add_overlay(MetaHero.crosshair.get_reel())
        # mark the route to target
        for step in self.get_route_to(
                *target_,
                max_area_=self.location.get_area()
        ):
            step_tile = self.location.get_tile_by_coordinates(*step)
            step_tile.add_overlay(MetaHero.crosshair_shadow.get_reel())

    def erase_targeting_line(self, target_):
        """
        erase marks on tiles that are in the line of sight to the target
        :param target_: coordinates of the target
        """
        # acquire target tile
        target_tile = self.location.get_tile_by_coordinates(*target_)
        # remove those parts of line of sight that has been displayed
        if target_tile:
            target_tile.remove_overlay(MetaHero.crosshair.get_reel())
        for step in self.get_route_to(
                *target_,
                max_area_=self.location.get_area()
        ):
            step_tile = self.location.get_tile_by_coordinates(*step)
            step_tile.remove_overlay(MetaHero.crosshair_shadow.get_reel(False))

    def beam(self):
        """
        choose target by freely moving the crosshair followed by broad beam
        """
        self.log.message('Choose target')
        # current position of crosshair
        crosshair_ = [self.get_x(), self.get_y()]

        direction_ = self._get_direction(confirm=True)

        while direction_:
            # once the target is confirmed retrieve its coordinates
            if direction_ is True:
                return crosshair_
            # aiming is being aborted
            elif direction_ is False:
                return False
            # if proper direction was chosen, change position of the crosshair
            else:

                crosshair_[0] += direction_[0]
                crosshair_[1] += direction_[1]

            # acquire target tile
            target_tile = self.location.get_tile_by_coordinates(*crosshair_)
            # draw line of sight
            if target_tile:
                # draw target mark
                target_tile.add_overlay(MetaHero.crosshair.get_reel())
                # draw route to target
                for step_ in self.get_beam_route_to(*crosshair_):
                    for sub_step in step_:
                        step_tile = self.location.get_tile_by_coordinates(*sub_step)
                        step_tile.add_overlay(MetaHero.crosshair_shadow.get_reel())

            direction_ = self._get_direction(confirm=True)

            # remove line of sight that has been displayed
            target_tile.remove_overlay(MetaHero.crosshair.get_reel())
            for step_ in self.get_beam_route_to(*crosshair_):
                for sub_step in step_:
                    step_tile = self.location.get_tile_by_coordinates(*sub_step)
                    step_tile.remove_overlay(MetaHero.crosshair_shadow.get_reel())

        # targeting aborted
        return False