from game_elements.element import Element

class Obstacle(Element):

    def __init__(self, width, height, x, y, color):
        super(Obstacle, self).__init__(width, height, x, y, color)

    def get_obstacle(self):
        return self.get_rectangle()