import pygame

from game_elements.game_figures.game_figure import GameFigure

class Dwarf(GameFigure):

    def __init__(self, width, height, x, y, color, table, health):
        super(Dwarf, self).__init__(width, height, x, y, color, table, health)
        self.__gold = 0

    def get_gold(self):
        return self.__gold

    def add_gold(self, amount):
        self.__gold += amount

    def catch_item(self, element):
        if (element.is_visible() and self._calculate_distance(element) >= self._calculate_distance(self)):
            if (type(element).__name__ == "Gold"):
                self.add_gold(element.get_amount())
            element.make_invisible()


    # Movement

    def increase_x(self):
        self._x += 1

    def decrease_x(self):
        self._x -= 1

    def increase_y(self):
        self._y += 1

    def decrease_y(self):
        self._y -= 1

    def move_dwarf(self, pressed, board):
        if pressed[pygame.K_UP] and (self._y - 1) > 0:
            self.decrease_y()
        if pressed[pygame.K_DOWN] and (self._y + 20) < board._height:
            self.increase_y()
        if pressed[pygame.K_RIGHT] and (self._x + 20) < board._width:
            self.increase_x()
        if pressed[pygame.K_LEFT] and (self._x - 1) > 0:
            self.decrease_x()