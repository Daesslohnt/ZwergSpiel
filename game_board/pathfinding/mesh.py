import pygame

from game_board.pathfinding.node import Node
from game_board.pathfinding.edge import Edge


class Mesh:

    def __init__(self, width, height, x_offset, y_offset, game_figure_width, game_figure_height, obstacles):
        self._width = width
        self._height = height
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._game_figure_width = game_figure_width
        self._game_figure_height = game_figure_height
        self._obstacles = obstacles
        self._nodes = []
        self._edges = []
        self.create_net()

    def create_net(self):
        # todo: how many are enough
        number_of_nodes_x = 10
        number_of_nodes_y = 10

        nodes = []

        x_step = (self._width - self._game_figure_width) // number_of_nodes_x
        y_step = (self._height - self._game_figure_height) // number_of_nodes_y

        for x in range(0, self._width - self._game_figure_width, x_step):
            for y in range(0, self._height - self._game_figure_height, y_step):
                if pygame.Rect(x + self._x_offset, y + self._y_offset, self._game_figure_width,
                               self._game_figure_height).collidelist(self._obstacles) == -1:
                    this_node = Node(x + self._x_offset, y + self._y_offset)
                    nodes.append(this_node)
                    for node in nodes:
                        if self.line_of_sight(this_node, node):
                            self._edges.append(Edge(node, this_node))
        self._nodes = nodes

    def get_nodes(self):
        return self._nodes

    def get_edges(self):
        return self._edges

    def get_xy(self):
        return self._x_offset, self._y_offset

    def get_size(self):
        return self._width, self._height

    def get_closest_node(self, xy):
        minimum_distance = self._width + self._height
        min_node = self._nodes[0]

        for node in self._nodes:
            node_xy = node.get_xy()
            distance_to_node = abs(xy[0] - node_xy[0] + xy[1] - node_xy[1])
            if distance_to_node < minimum_distance:
                minimum_distance = distance_to_node
                min_node = node

        return min_node

    def get_neighbouring_nodes(self, node):
        neighbouring_nodes = []
        for edge in self._edges:
            edge_nodes = edge.get_nodes()
            if edge_nodes[0] == node:
                neighbouring_nodes.append(edge_nodes[1])
            elif edge_nodes[1] == node:
                neighbouring_nodes.append(edge_nodes[0])

        return neighbouring_nodes

    def line_of_sight(self, node1, node2):
        line_of_sight = True
        line_left_top = node1.get_xy() + node2.get_xy()
        line_right_top = node1.get_xy()[0] + self._game_figure_width, node1.get_xy()[1], \
                         node2.get_xy()[0] + self._game_figure_width, node2.get_xy()[1]
        line_left_bottom = node1.get_xy()[0], node1.get_xy()[1] + self._game_figure_height, \
                           node2.get_xy()[0], node2.get_xy()[1] + self._game_figure_height
        line_right_bottom = node1.get_xy()[0] + self._game_figure_width, node1.get_xy()[1] + self._game_figure_height, \
                            node2.get_xy()[0] + self._game_figure_width, node2.get_xy()[1] + self._game_figure_height

        for obstacle in self._obstacles:
            if len(obstacle.clipline(line_left_top)) != 0:
                line_of_sight = False
            elif len(obstacle.clipline(line_left_bottom)) != 0:
                line_of_sight = False
            elif len(obstacle.clipline(line_right_top)) != 0:
                line_of_sight = False
            elif len(obstacle.clipline(line_right_bottom)) != 0:
                line_of_sight = False

            if not line_of_sight:
                break

        return line_of_sight
