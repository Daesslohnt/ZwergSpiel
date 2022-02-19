import pygame

from game_elements.obstracles.border import Border

class UpDownBorder(Border):
    UP_DOWN_BORDER = pygame.transform.scale(pygame.image.load('sorce/border_stone.jpg'), (600, 30))

    def __init__(self, width, height, x, y, color):
        super(UpDownBorder, self).__init__(width, height, x, y, color)