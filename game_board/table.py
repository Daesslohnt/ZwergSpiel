import pygame
import random
import time

from game_elements.game_figures.dwarf import Dwarf
from game_elements.items.gold import Gold
from game_elements.game_figures.kobold import Kobold
from game_elements.items.exit import Exit


class Table(object):
    DWARF_IMG = pygame.image.load('sorce/zwerg.jpg')
    DWARF_IMG = pygame.transform.scale(DWARF_IMG, (20, 20))
    KOBOLD_IMG = pygame.image.load('sorce/kobold.jpg')
    KOBOLD_IMG = pygame.transform.scale(KOBOLD_IMG, (20, 20))

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

    def create_exit(self):
        self.exit = Exit(40, 15, 280, 30, (40, 60, 237), self)

    def draw_exit(self):
        pygame.draw.rect(self.screen,
                         self.exit.get_color(),
                         self.exit.get_item_rect())

    def get_exit(self):
        return self.exit

    def create_dwarf(self):
        x = self._height // 2
        y = self._width // 2
        color = (227, 99, 25)
        self.__dwarf = Dwarf(20, 20, x, y, color, self, 5)

    def draw_dwarf(self, screen):
        pygame.draw.rect(self.screen,
                         self.__dwarf.get_color(),
                         self.__dwarf.get_rect()
                         )
        screen.blit(self.DWARF_IMG, self.__dwarf.get_xy())

    def get_dwarf(self):
        return self.__dwarf

    def create_gold(self, count):
        color = (208, 242, 15)
        self.gold_counter = count
        self.gold_mountains = list()
        for i in range(count):
            x = random.randint(30, self._width-30)
            y = random.randint(30, self._height-30)
            gold_i = Gold(10, 10, x, y, color, self, 100)
            self.gold_mountains.append((gold_i, gold_i.get_item_rect()))

    def get_gold_counter(self):
        return self.gold_counter

    def draw_gold(self, i):
        pygame.draw.rect(self.screen,
                         self.gold_mountains[i][0].get_color(),
                         self.gold_mountains[i][1]
                         )

    def get_gold_items(self, i):
        return self.gold_mountains[i][0]

    def get_gold_items_rect(self, i):
        return self.gold_mountains[i][1]

    def create_kobolds(self, counter):
        color = (39, 176, 26)
        self.kobold_counter = counter
        self.kobolds = list()
        for i in range(counter):
            x = random.randint(40, self._width - 40)
            y = random.randint(40, self._height - 40)
            kobold_i = Kobold(20, 20, x, y, color, self, 10)
            self.kobolds.append([kobold_i, kobold_i.get_rect()])

    def get_kobold_counter(self):
        return self.kobold_counter

    def draw_kobolds(self, i, screen):
        self.kobolds[i][1] = self.kobolds[i][0].get_rect()
        pygame.draw.rect(self.screen, self.kobolds[i][0].get_color(), self.kobolds[i][1])
        screen.blit(self.KOBOLD_IMG, self.kobolds[i][0].get_xy())


    #return list [Kobold, Rect]
    def get_kobold(self, i):
        return self.kobolds[i]

    def collision(self, obj1, obj2):
        return obj1.colliderect(obj2)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (250, 0, 0))
        return textSurface, textSurface.get_rect()

    def message_display(self, text, screen):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self._width / 2), (self._height / 2))
        screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

