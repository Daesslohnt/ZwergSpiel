from pygame.rect import Rect


class Node:
    def __init__(self, x, y):
        self._x = x
        self._y = y

        print_size = 10
        self._rect = Rect(x - print_size / 2, y - print_size / 2, print_size, print_size)

    def get_xy(self):
        return self._x, self._y

    def get_rect(self):
        return self._rect
