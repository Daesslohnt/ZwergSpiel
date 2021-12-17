from game_board.game_logic import GameLogic
from game_elements.items.item import Item

class Exit(Item):

    def __init__(self, width, height, x, y, color, table):
        super(Exit, self).__init__(width, height, x, y, color, table)
