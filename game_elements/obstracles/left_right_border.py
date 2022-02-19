import pygame

from game_elements.obstracles.border import Border

class LeftRightBorder(Border):
    LEFT_RIGHT_BORDER = pygame.transform.scale(pygame.image.load('sorce/border_stone.jpg'), (30, 600))

    def __init__(self, width, height, x, y, color):
        super(LeftRightBorder, self).__init__(width, height, x, y, color)