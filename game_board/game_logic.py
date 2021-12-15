

class GameLogic:

    def __init__(self):
        self._gold_cached = 0
        self._is_win = False

    def logic(self, exit):
        if (exit):
            self._is_win = True

    def get_is_win(self):
        return self._is_win

    """
    as parameter get all gold that the dwarf has
    """
    def catch_some_gold(self, amount):
        self._gold_cached += amount - self._gold_cached

    def get_cached_gold(self):
        return self._gold_cached