import pygame
import random

from game_elements.game_figures.dwarf import Dwarf
from game_elements.items.gold import Gold
#from game_elements.game_figures.

class Table(object):

    def __init__(self, width, height, screen):
        self._width = width
        self._height = height
        self.screen = screen

    def get_size(self):
        return self._width, self._height

    def empty_board(self):
        self.screen.fill((0, 0, 0))

    def create_dwarf(self):
        x = self._height // 2
        y = self._width // 2
        color = (227, 99, 25)
        self.__dwarf = Dwarf(20, 20, x, y, color, self, 5)

    def draw_dwarf(self):
        pygame.draw.rect(self.screen,
                         self.__dwarf.get_color(),
                         (self.__dwarf.get_xy()[0],
                          self.__dwarf.get_xy()[1],
                          self.__dwarf.get_size()[0],
                          self.__dwarf.get_size()[1])
                         )

    def get_dwarf(self):
        return self.__dwarf

    def create_kobold(self):
        pass

    def create_gold(self):
        color = (208, 242, 15)
        self.gold_mountains = list()
        for i in range(3):
            x = random.randint(10, self._width)
            y = random.randint(10, self._height)
            self.gold_mountains.append(Gold(10, 10, x, y, color, self, 100))

    def draw_gold(self, i):
        pygame.draw.rect(self.screen,
                         self.gold_mountains[i].get_color(),
                         (self.gold_mountains[i].get_xy()[0],
                          self.gold_mountains[i].get_xy()[1],
                          self.gold_mountains[i].get_size()[0],
                          self.gold_mountains[i].get_size()[1])
                         )

    def get_gold_items(self):
        return self.gold_mountains