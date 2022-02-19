import pygame
import logging

from game_elements.game_figures.game_figure import GameFigure
from utils.json_parser import JsonParser

config = JsonParser.parse_constatns()
logging.basicConfig(filename='sorce/history.log', level=logging.INFO)

class Dwarf(GameFigure):
    DWARF_IMG = pygame.transform.scale(pygame.image.load('sorce/zwerg.jpg'),
                                       (config['dwarf_size']['width'], config['dwarf_size']['height']))

    def __init__(self, width, height, x, y, color, health):
        super(Dwarf, self).__init__(width, height, x, y, color, health)
        self._cached_gold = 0

    def get_gold(self):
        return self._cached_gold

    def add_gold(self, amount):
        self._cached_gold += amount

    def catch_item(self, element, game_logic):
        """
        increment collected gold and make it invisible
        or set game to win if dwarf collide exit

        :param element: game element that dwarf collides
        :param game_logic: obj to set it win if possible
        :return: None
        """
        if (element.is_visible() and self.check_collision(element.get_rectangle())):
            if (type(element).__name__ == "Gold"):
                self.add_gold(element.get_amount())
                element.make_invisible()
                self.add_gold(element.get_amount())
                message = 'collected {}'.format(element.get_amount)
                logging.info(message)
            if (type(element).__name__ == "Exit"):
                game_logic.set_to_win()
                logging.info('exit')

    def get_dwarf_rect(self):
        return self.get_game_figure_rect()

    def move_dwarf(self, pressed, right, left, up, down):
        if pressed[pygame.K_UP] and not up:
            self.decrease_y()
        if pressed[pygame.K_DOWN] and not down:
            self.increase_y()
        if pressed[pygame.K_RIGHT] and not right:
            self.increase_x()
        if pressed[pygame.K_LEFT] and not left:
            self.decrease_x()