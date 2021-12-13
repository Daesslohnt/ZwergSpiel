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

    def catch_item(self, element, elem_rect):
        if (element.is_visible() and self.check_collision(elem_rect)):
            if (type(element).__name__ == "Gold"):
                self.add_gold(element.get_amount())
            element.make_invisible()
            print("collected")

    def get_rect(self):
        self.dwarf_rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self.dwarf_rect

    # Movement

    def increase_x(self):
        self._x += 1

    def decrease_x(self):
        self._x -= 1

    def increase_y(self):
        self._y += 1

    def decrease_y(self):
        self._y -= 1

    def move_dwarf(self, pressed, right, left, up, down):
        if pressed[pygame.K_UP] and not up:
            self.decrease_y()
        if pressed[pygame.K_DOWN] and not down:
            self.increase_y()
        if pressed[pygame.K_RIGHT] and not right:
            self.increase_x()
        if pressed[pygame.K_LEFT] and not left:
            self.decrease_x()