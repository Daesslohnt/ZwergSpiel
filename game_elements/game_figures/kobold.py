import random
import pygame

from game_elements.game_figures.game_figure import GameFigure
from game_elements.items.axe import Axe
from utils.json_parser import JsonParser

config = JsonParser.parse_constatns()

class Kobold(GameFigure):
    KOBOLD_IMG = pygame.transform.scale(pygame.image.load('sorce/kobold.jpg'),
                                        (config['kobold_size']['width'], config['kobold_size']['height']))

    def __init__(self, width, height, x, y, color, health):
        super(Kobold, self).__init__(width, height, x, y, color, health)
        self._item = Axe(10, 10, 300, 300, (1, 0, 0))

    def move_kobold(self, dwarf):
        direction_v = random.randint(0, 1)
        if (direction_v):
            if (dwarf.get_xy()[1] > self._y):
                self.increase_y()
            else:
                self.decrease_y()
        else:
            if (dwarf.get_xy()[0] < self._x):
                self.decrease_x()
            else:
                self.increase_x()

    def get_kobold_rect(self):
        return self.get_game_figure_rect()

    def catch_item(self, element, game_logic):
        if (type(element).__name__ == "Dwarf" and self.check_collision(element.get_rectangle())):
            print("dwarf is cached", self.get_xy())
            game_logic.set_to_lose()
