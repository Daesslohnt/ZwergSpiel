from game_elements.element import Element

class Item(Element):

    def __init__(self, width, height, x, y, color, table):
        super(Item, self).__init__(width, height, x, y, color, table)
        self.__is_visible = True

    def is_visible(self):
        return self.__is_visible

    def make_invisible(self):
        self.__is_visible = False