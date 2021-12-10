

class Element(object):

    """:cvar
    :parameter
        width: int for game figures mus be 20 for items 10, for landmass 20
        height: int for game figures mus be 20 for items 10, for landmass 20
        x, y:  start coordinates must be in table within element's size
        color: (int[0-255], int[0-255], int[0-255]) RGB color of element
        table: object screen, where the element will be placed
    """
    def __init__(self, width, height, x, y, color, table):
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        self.__color = color
        self._table = table
        if ((self._x + self._width // 2) >= self._table.get_size()[0]
        or (self._x - self._width // 2) < 0
        or (self._y + self._height // 2) >= self._table.get_size()[1]
        or (self._y + self._height // 2) < 0):
            raise Exception

    def get_size(self):
        return self._width, self._height

    def get_xy(self):
        return self._x, self._y

    def get_color(self):
        return self.__color