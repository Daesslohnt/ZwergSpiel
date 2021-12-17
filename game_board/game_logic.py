

class GameLogic:
    WIN = False
    LOSE = False

    def __init__(self):
        self._gold_cached = 0


    def set_to_win(self):
        self.WIN = True

    def set_to_lose(self):
        self.LOSE = True

    def get_is_win(self):
        return self.WIN

    def get_is_lose(self):
        return self.LOSE

    """
    as parameter get all gold that the dwarf has
    """
    def catch_some_gold(self, amount):
        self._gold_cached += amount - self._gold_cached

    def get_cached_gold(self):
        return self._gold_cached