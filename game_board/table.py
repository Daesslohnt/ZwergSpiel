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

    def set_borders(self):
        self.up_border = pygame.Rect(0, 0, self._width, 30)
        self.down_border = pygame.Rect(0, self._height-30, self._width, 30)
        self.left_border = pygame.Rect(0, 0, 30, self._height)
        self.right_border = pygame.Rect(self._width-30, 0, 30, self._height)

    def up_border_collision(self):
        return self.__dwarf.get_rect().colliderect(self.up_border)

    def down_border_collision(self):
        return self.__dwarf.get_rect().colliderect(self.down_border)

    def right_border_collision(self):
        return self.__dwarf.get_rect().colliderect(self.right_border)

    def left_border_collision(self):
        return self.__dwarf.get_rect().colliderect(self.left_border)

    def draw_borders(self, screen):
        pygame.draw.rect(screen, (250, 0, 30), self.right_border)
        pygame.draw.rect(screen, (250, 0, 30), self.left_border)
        pygame.draw.rect(screen, (250, 0, 30), self.up_border)
        pygame.draw.rect(screen, (250, 0, 30), self.down_border)

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
                         self.__dwarf.get_rect()
                         )

    def get_dwarf(self):
        return self.__dwarf

    def create_kobold(self):
        pass

    def create_gold(self):
        color = (208, 242, 15)
        self.gold_mountains = list()
        for i in range(3):
            x = random.randint(30, self._width-30)
            y = random.randint(30, self._height-30)
            gold_i = Gold(10, 10, x, y, color, self, 100)
            self.gold_mountains.append((gold_i, gold_i.get_item_rect()))

    def draw_gold(self, i):
        pygame.draw.rect(self.screen,
                         self.gold_mountains[i][0].get_color(),
                         self.gold_mountains[i][1]
                         )

    def get_gold_items(self, i):
        return self.gold_mountains[i][0]

    def get_gold_items_rect(self, i):
        return self.gold_mountains[i][1]

    def collision(self, obj1, obj2):
        return obj1.colliderect(obj2)