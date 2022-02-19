from game_elements.obstracles.obstacle import Obstacle

class Border(Obstacle):

    def __init__(self, width, height, x, y, color):
        super(Border, self).__init__(width, height, x, y, color)

    def get_border(self):
        return self.get_obstacle()