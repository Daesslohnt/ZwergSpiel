import pygame

from game_elements.items.item import Item
from utils.json_parser import JsonParser

config = JsonParser.parse_constatns()

class Gold(Item):
    GOLD_IMG = pygame.transform.scale(pygame.image.load('sorce/gold.jpg'),
                                      (config['gold_size']['width'], config['gold_size']['height']))

    def __init__(self, width, height, x, y, color, amount):
        super(Gold, self).__init__(width, height, x, y, color)
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_gold_rect(self):
        return self.get_item_rect()