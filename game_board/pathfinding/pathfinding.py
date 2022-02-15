from game_board.pathfinding.mesh import Mesh
import math


def distance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


class Pathfinding:

    def __init__(self, width, height, x_offset, y_offset, game_figure_width, game_figure_height, obstacle_as_rect_list):
        self._mesh = Mesh(width, height, x_offset, y_offset,
                          game_figure_width, game_figure_height, obstacle_as_rect_list)

    def find_next_movement(self, start, end):
        if distance(start, end) < distance(start, self._mesh.get_closest_node(start).get_xy()):
            return end
        else:
            next_node = self._mesh.get_closest_node(start)
            possible_nodes = self._mesh.get_neighbouring_nodes(self._mesh.get_closest_node(start))
            closest_node_to_end = next_node

            minimum_distance_to_end = distance(end, next_node.get_xy())

            for node in possible_nodes:
                if minimum_distance_to_end > distance(end, node.get_xy()):
                    minimum_distance_to_end = distance(end, node.get_xy())
                    closest_node_to_end = node

            return closest_node_to_end.get_xy()

    def get_mesh(self):
        return self._mesh
