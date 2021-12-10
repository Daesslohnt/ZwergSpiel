from game_elements.items.item import Item

class Gold(Item):

    def __init__(self, width, height, x, y, color, table, amount):
        super(Gold, self).__init__(width, height, x, y, color, table)
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount