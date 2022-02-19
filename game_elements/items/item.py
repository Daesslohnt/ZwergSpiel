from game_elements.element import Element

class Item(Element):

    def __init__(self, width, height, x, y, color):
        """
        General object for all items
        items can be visible or invisible

        :param width: the width of item
        :param height: the height of item
        :param x: left coordinate
        :param y: top coordinate
        :param color:
        """
        super(Item, self).__init__(width, height, x, y, color)
        self.__is_visible = True

    def is_visible(self):
        """return True if item is visible"""
        return self.__is_visible

    def make_invisible(self):
        """set item to invisible"""
        self.__is_visible = False

    def get_item_rect(self):
        """get rectangle of the item"""
        return self.get_rectangle()