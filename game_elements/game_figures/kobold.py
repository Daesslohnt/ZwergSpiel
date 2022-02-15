import random
import pygame

from game_elements.game_figures.game_figure import GameFigure
from game_elements.items.axe import Axe

class Kobold(GameFigure):

    def __init__(self, width, height, x, y, color, table, health):
        super(Kobold, self).__init__(width, height, x, y, color, table, health)
        self._item = Axe(10, 10, 300, 300, (1, 0,0), table)

    def move_kobold(self, dwarf, pathfinding):
        direction_v = random.randint(0, 1) == 0
        movement_coordinates_xy = dwarf.get_xy()
        movement_coordinates_xy = pathfinding.find_next_movement(self.get_xy(),dwarf.get_xy())
        if (direction_v):
            if (movement_coordinates_xy[1] > self._y):
                self.increase_y()
            elif (movement_coordinates_xy[1] < self._y):
                self.decrease_y()
        else:

            if (movement_coordinates_xy[0] < self._x):
                self.decrease_x()
            elif (movement_coordinates_xy[0] > self._x):
                self.increase_x()

    def get_rect(self):
        self.kobold_rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return self.kobold_rect

    def catch_item(self, element, collision, game_logic):
        if (collision and type(element).__name__ == "Dwarf"):
            game_logic.set_to_lose()
