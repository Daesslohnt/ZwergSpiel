from game_elements.items.item import Item

class Axe(Item):

    def __init__(self, width, height, x, y, color, table):
        super(Axe, self).__init__(width, height, x, y, color, table)
        self._damage = 10

    def use_weapon(self):
        return self._damage