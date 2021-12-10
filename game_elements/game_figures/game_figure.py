import math

from game_elements.element import Element

class GameFigure(Element):

    def __init__(self, width, height, x, y, color, table, health):
        super(GameFigure, self).__init__(width, height, x, y, color, table)
        self.__health = health
        self.__item = None
        self.__is_alive = True
        self.__is_visible = True

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

    def catch_item(self, element):
        if (element.is_visible() and self._calculate_distance(element) >= self._calculate_distance(self)):
            self.item = element
            element.set_invisible()

    def _calculate_distance(self, item):
        return math.sqrt(item.get_xy()[0] ** 2 + item.get_xy()[1] ** 2)