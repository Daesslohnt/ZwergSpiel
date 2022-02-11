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
        self._clock = pygame.time.Clock()

    def set_up_screen(self, length, width):
        self.length = length
        self.width = width
        self.screen = pygame.display.set_mode([length, width])

    def set_board(self):
        self.board = Table(self.length, self.width, self.screen)
        self.board.set_borders()

    def set_game_logic(self):
        self.game_logic = GameLogic()

    def create_all_elements(self, golds, kobolds):
        self.board.create_dwarf()
        self.board.create_exit()
        self.board.create_gold(golds)
        self.board.create_kobolds(kobolds)

    def game_action(self):
        while not self.game_logic.get_is_lose() and not self.game_logic.get_is_win():
            #time delay
            self._clock.tick(config["FPS"])
            time.sleep(config["delay"])

            #its how to exit the game before you lose
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit()

            #help to manipulate figure with your keys
            pressed = pygame.key.get_pressed()

            #draw the board borders
            self.board.empty_board()
            self.board.draw_borders(self.screen)
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

            self.board.draw_dwarf(self.screen)

            # Kobolds
            for i in range(self.board.get_kobold_counter()):
                self.board.get_kobold(i)[0].move_kobold(self.board.get_dwarf())
                self.board.get_kobold(i)[0].catch_item(self.board.get_dwarf(),
                                                       self.board.collision(self.board.get_kobold(i)[1],
                                                                            self.board.get_dwarf().get_rect()),
                                                       self.game_logic)
                self.board.draw_kobolds(i, self.screen)

            # Gold
            for i in range(self.board.get_gold_counter()):
                self.board.get_dwarf().catch_item(self.board.get_gold_items(i),
                                                  self.board.collision(self.board.get_dwarf().get_rect(),
                                                                        self.board.get_gold_items_rect(i)),
                                                                        self.game_logic)
                if (self.board.get_gold_items(i).is_visible()):
                    self.board.draw_gold(i)

            # game logic
            self.game_logic.catch_some_gold(self.board.get_dwarf().get_gold())

            #update the screen
            pygame.display.update()

        #after the game ends
        if (self.game_logic.get_is_lose()):
            self.board.empty_board()
            self.board.message_display("Lose !!!", self.screen)
        elif (self.game_logic.get_is_win()):
            self.board.empty_board()
            self.board.message_display("You Won!!!", self.screen)
        else:
            raise Exception