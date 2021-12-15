import random
import pygame

from game_elements.game_figures.game_figure import GameFigure
from game_elements.items.axe import Axe

class Kobold(GameFigure):

    def __init__(self, width, height, x, y, color, table, health):
        super(Kobold, self).__init__(width, height, x, y, color, table, health)
        self._item = Axe(10, 10, 300, 300, (1, 0,0), table)

    def move_kobold(self, dwarf):
        direction_v = random.randint(0, 1) == 0
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

    def get_rect(self):
        self.kobold_rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self.kobold_rect

    def catch_item(self, element, collision):
        if (collision and type(element).__name__ == "Dwarf"):
            return True