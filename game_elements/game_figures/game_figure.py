import pygame

from game_elements.element import Element

class GameFigure(Element):

    def __init__(self, width, height, x, y, color, health):
        super(GameFigure, self).__init__(width, height, x, y, color)
        self.__health = health
        self.__item = None
        self.__is_alive = True
        self.__is_visible = True

    def get_game_figure_rect(self):
        return self.get_rectangle()

    def get_hp(self):
        return self.__health

    def set_health(self, hp):
        self.__health = hp

    def take_damage(self, damage):
        self.__health -= damage

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item

    # Movement

    def increase_x(self):
        self._x += 1

    def decrease_x(self):
        self._x -= 1

    def increase_y(self):
        self._y += 1

    def decrease_y(self):
        self._y -= 1

    def check_collision(self, another_rect):
        return self.get_game_figure_rect().colliderect(another_rect)