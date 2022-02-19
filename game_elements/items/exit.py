import pygame

from game_elements.items.item import Item
from utils.json_parser import JsonParser

config = JsonParser.parse_constatns()

class Exit(Item):
    EXIT = pygame.transform.scale(pygame.image.load('sorce/exit.jpg'),
                                  (config['exit_size']['width'], config['exit_size']['height']))

    def __init__(self, width, height, x, y, color):
        super(Exit, self).__init__(width, height, x, y, color)