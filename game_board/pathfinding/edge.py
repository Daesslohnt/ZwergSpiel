import math


def distance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


class Edge:
    def __init__(self, node1, node2):
        self._nodes = node1, node2
        self._distance = distance(self._nodes[0].get_xy(),
                                  self._nodes[1].get_xy())

    def get_nodes(self):
        return self._nodes

    def get_distance(self):
        return self._distance
