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

    def catch_item(self, element, collision, game_logic):
        if (element.is_visible() and collision):
            if (type(element).__name__ == "Gold"):
                self.add_gold(element.get_amount())
                element.make_invisible()
                self.add_gold(100)
                print("collected")
            if (type(element).__name__ == "Exit"):
                game_logic.set_to_win()
                print("exit collision")

    def get_rect(self):
        self.dwarf_rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self.dwarf_rect

    def move_dwarf(self, pressed, right, left, up, down):
        if pressed[pygame.K_UP] and not up:
            self.decrease_y()
        if pressed[pygame.K_DOWN] and not down:
            self.increase_y()
        if pressed[pygame.K_RIGHT] and not right:
            self.increase_x()
        if pressed[pygame.K_LEFT] and not left:
            self.decrease_x()