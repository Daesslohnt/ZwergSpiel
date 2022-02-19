import pygame
import random
import time

from game_elements.game_figures.dwarf import Dwarf
from game_elements.items.gold import Gold
from game_elements.game_figures.kobold import Kobold
from game_elements.items.exit import Exit
from game_elements.obstracles.up_down_border import UpDownBorder
from game_elements.obstracles.left_right_border import LeftRightBorder
from utils.json_parser import JsonParser

const = JsonParser.parse_constatns()
config = JsonParser.parse_configuration()


class Table(object):
    FLOOR = pygame.transform.scale(pygame.image.load('sorce/floortexture.jpg'),
                                   (config['screen_size'], config['screen_size']))

    def __init__(self, width, height, screen):
        self._width = width
        self._height = height
        self.screen = screen

    def set_borders(self) -> None:
        """
        create recatangles for borders

        :return: None
        """
        self.up_border = UpDownBorder(self._width, 30, 0, 0, (255, 255, 255))
        self.down_border = UpDownBorder(self._width, 30, 0, self._height-30, (255, 255, 255))
        self.left_border = LeftRightBorder(30, self._height, 0, 0, (255, 255, 255))
        self.right_border = LeftRightBorder(30, self._height, self._width-30, 0, (255, 255, 255))

    def up_border_collision(self):
        """
        check that dwarf collide upper border

        :return:
        boolean: collision to upper border
        """
        return self.__dwarf.get_dwarf_rect().colliderect(self.up_border.get_rectangle())

    def down_border_collision(self):
        """
        check that dwarf collide down border

        :return: boolean: collision to down border
        """
        return self.__dwarf.get_dwarf_rect().colliderect(self.down_border.get_rectangle())

    def right_border_collision(self):
        """
        check thad dwarf collides right border

        :return: boolean: dwarf collides right border
        """
        return self.__dwarf.get_dwarf_rect().colliderect(self.right_border.get_rectangle())

    def left_border_collision(self):
        """
        check that dwarf collides left border

        :return: boolean: dwarf collides left border
        """
        return self.__dwarf.get_dwarf_rect().colliderect(self.left_border.get_rectangle())

    def draw_borders(self):
        """draw borders on the screen"""
        self.screen.blit(self.right_border.LEFT_RIGHT_BORDER, (self._width-30, 0))
        self.screen.blit(self.left_border.LEFT_RIGHT_BORDER, (0, 0))
        self.screen.blit(self.up_border.UP_DOWN_BORDER, (0, 0))
        self.screen.blit(self.down_border.UP_DOWN_BORDER, (0, self._height-30))

    def get_size(self):
        """
        get size of the table = screen

        :return: tuple (width, height)
        """
        return self._width, self._height

    def empty_board(self):
        """set screen to black"""
        self.screen.fill((0, 0, 0))

    def draw_dungeon_floor(self):
        """draw floor texture on the screen"""
        self.screen.blit(self.FLOOR, (0, 0))

    def create_exit(self):
        """create exit object"""
        self._exit = Exit(const['exit_size']['width'], const['exit_size']['height'], 280, 30, (40, 60, 237))

    def draw_exit(self):
        """Draw the exit on the screen"""
        self.screen.blit(self._exit.EXIT, self._exit.get_xy())

    def get_exit(self):
        """:return: object of exit"""
        return self._exit

    def create_dwarf(self):
        """create dwarf on the middle of the screen"""
        x = self._height // 2
        y = self._width // 2
        color = (227, 99, 25)
        self.__dwarf = Dwarf(const['dwarf_size']['width'], const['dwarf_size']['height'], x, y, color, 5)

    def draw_dwarf(self):
        """draw the dwarf on the screen"""
        # pygame.draw.rect(self.screen, self.__dwarf.get_color(), self.__dwarf.get_dwarf_rect())
        self.screen.blit(self.__dwarf.DWARF_IMG, self.__dwarf.get_xy())

    def get_dwarf(self):
        """get dwarf object"""
        return self.__dwarf

    def create_gold(self, count):
        """
        create predefined count of gold items and record them in self.gold_mountains

        :param count: predefined count of gold items to be created
        :return: None
        """
        color = (208, 242, 15)
        self.gold_counter = count
        self.gold_mountains = list()
        for i in range(count):
            x = random.randint(30, self._width-30)
            y = random.randint(30, self._height-30)
            gold_i = Gold(const['gold_size']['width'], const['gold_size']['height'], x, y, color, 100)
            self.gold_mountains.append(gold_i)

    def get_gold_counter(self):
        """get amount of created gold items"""

        return self.gold_counter

    def draw_gold(self, i):
        """draw gold item number i from self.gold_mountains"""
        pygame.draw.rect(self.screen, self.gold_mountains[i].get_color(), self.gold_mountains[i].get_gold_rect())
        self.screen.blit(self.gold_mountains[i].GOLD_IMG, self.gold_mountains[i].get_xy())

    def get_gold_items(self, i):
        """get list of gold items"""
        return self.gold_mountains[i]

    def create_kobolds(self, counter):
        """
        create predefined count of kobolds in self.kobolds

        :param counter: amount of kobolds to be created
        :return: None
        """
        color = (39, 176, 26)
        self.kobold_counter = counter
        self.kobolds = list()
        for i in range(counter):
            x = random.randint(40, self._width - 40)
            y = random.randint(40, self._height - 40)
            kobold_i = Kobold(const['kobold_size']['width'], const['kobold_size']['height'], x, y, color, 10)
            self.kobolds.append(kobold_i)

    def get_kobold_counter(self):
        """get count of created kobolds"""
        return self.kobold_counter

    def draw_kobolds(self, i):
        """draw kobolds"""
        self.screen.blit(self.kobolds[i].KOBOLD_IMG, self.kobolds[i].get_xy())

    def get_kobold_by_index(self, i):
        """
        get kobold tuple of (kobold object, kobold rectangle)

        :param i: number of kobold in self.kobolds
        :return: tuple(kobold obj, rect)
        """
        return self.kobolds[i]

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (250, 0, 0))
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((self._width / 2), (self._height / 2))
        self.screen.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)