import pygame

from game_elements.element import Element

class GameFigure(Element):

    def __init__(self, width, height, x, y, color, table, health):
        super(GameFigure, self).__init__(width, height, x, y, color, table)
        self.__health = health
        self.__item = None
        self.__is_alive = True
        self.__is_visible = True
        self.fig_rect = self.create_rect()

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

    def create_rect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)

    def catch_item(self, element, elem_rect):
        if (element.is_visible() and self.check_collision(elem_rect)):
            element.make_invisible()
            print("collected")

    def check_collision(self, rect):
        return self.fig_rect.colliderect(rect)