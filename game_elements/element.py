import pygame

from utils.json_parser import JsonParser

config = JsonParser.parse_configuration()

class Element(object):

    def __init__(self, width, height, x, y, color):
        """
        general game element, define size and left top coordinates of object
        and color
        if element appears out of border raise exception

        :parameter
            width: int for game figures mus be 20 for items 10, for landmass 20
            height: int for game figures mus be 20 for items 10, for landmass 20
            x, y:  start coordinates must be in table within element's size
            color: (int[0-255], int[0-255], int[0-255]) RGB color of element
        """
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        self._color = color
        if ((self._x + self._width) > config['screen_size']
        or self._x < 0
        or (self._y + self._height) > config['screen_size']
        or self._y < 0):
            raise Exception
        self._rectangle = pygame.Rect(x, y, width, height)

    def update_rect_xy(self):
        self._rectangle = pygame.Rect(self._x, self._y, self._width, self._height)

    def get_size(self):
        """get object size tuple (width, height)"""
        return self._width, self._height

    def get_xy(self):
        """get coordinates of object tuple (x, y)"""
        return (self._x, self._y)

    def get_params(self):
        """get all parameters of element tuple (x, y, width, height)"""
        return self._x, self._y, self._width, self._height

    def get_color(self):
        """get color tuple (R, G, B)"""
        return self._color

    def get_rectangle(self):
        """get rectangle of object"""
        return self._rectangle