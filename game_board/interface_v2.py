import pygame
import sys
import time

from game_board.table import Table
from game_board.game_logic import GameLogic
from utils.json_parser import JsonParser

config = JsonParser.parse()


class Interface:

    def __init__(self):
        pygame.init()

    def set_up_screen(self, length, width):
        self.length = length
        self.width = width
        self.screen = pygame.display.set_mode([length, width])

    def set_board(self):
        self.board = Table(self.length, self.width, self.screen)
        self.board.set_borders()
        self.board.create_pathfinding()

    def set_game_logic(self):
        self.game_logic = GameLogic()

    def create_all_elements(self, golds, kobolds):
        self.board.create_dwarf()
        self.board.create_exit()
        self.board.create_gold(golds)
        self.board.create_kobolds(kobolds)

    def game_action(self):
        while not self.game_logic.get_is_lose() and not self.game_logic.get_is_win():
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit()

            pressed = pygame.key.get_pressed()
            self.board.empty_board()
            self.board.draw_obstacles(self.screen)
            self.board.draw_exit()

            # Dwarf
            self.board.get_dwarf().move_dwarf(pressed,
                                              self.board.right_border_collision(),
                                              self.board.left_border_collision(),
                                              self.board.up_border_collision(),
                                              self.board.down_border_collision())
            self.board.get_dwarf().catch_item(self.board.get_exit(),
                                              self.board.collision(self.board.get_dwarf().get_rect(),
                                                                   self.board.get_exit().get_item_rect()),
                                              self.game_logic)

            self.board.draw_dwarf()

            # Kobolds
            for i in range(self.board.get_kobold_counter()):
                self.board.get_kobold(i)[0].move_kobold(self.board.get_dwarf(), self.board.get_pathfinding())
                self.board.get_kobold(i)[0].catch_item(self.board.get_dwarf(),
                                                       self.board.collision(self.board.get_kobold(i)[1],
                                                                            self.board.get_dwarf().get_rect()),
                                                       self.game_logic)
                self.board.draw_kobolds(i)

            # Gold
            for i in range(self.board.get_gold_counter()):
                self.board.get_dwarf().catch_item(self.board.get_gold_items(i),
                                                  self.board.collision(self.board.get_dwarf().get_rect(),
                                                                       self.board.get_gold_items_rect(i)),
                                                  self.game_logic)
                if (self.board.get_gold_items(i).is_visible()):
                    self.board.draw_gold(i)

            #debug
            if config["debug_pathfinding"]:
                self.board.draw_pathfinding()

            # game logic
            self.game_logic.catch_some_gold(self.board.get_dwarf().get_gold())
            time.sleep(config["delay"])
            pygame.display.update()

        if (self.game_logic.get_is_lose()):
            self.board.empty_board()
            self.board.message_display("Lose !!!", self.screen)
        elif (self.game_logic.get_is_win()):
            self.board.empty_board()
            self.board.message_display("You Won!!!", self.screen)
        else:
            raise Exception


if __name__ == '__main__':
    interface = Interface()
    interface.set_up_screen(config["screen_size"], config["screen_size"])
    interface.set_board()
    interface.create_all_elements(config["count_of_gold"], config["count_of_kobolds"])
    interface.set_game_logic()
    interface.game_action()
