import pygame

from game_elements.element import Element

class Item(Element):

    def __init__(self, width, height, x, y, color, table):
        super(Item, self).__init__(width, height, x, y, color, table)
        self.__is_visible = True
        self.item_rect = self.create_item_rect()

    def is_visible(self):
        return self.__is_visible

    def make_invisible(self):
        self.__is_visible = False

    def create_item_rect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)

    def get_item_rect(self):
        return self.item_rect