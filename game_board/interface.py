import pygame
import sys
import time

from game_board.table import Table

class Interface:

    def __init__(self):
        pygame.init()

    def set_up_screen(self, length, width):
        self.length = length
        self.width = width
        self.screen = pygame.display.set_mode([length, width])

    def set_board(self):
        self.board = Table(600, 600, self.screen)

    def create_all_elements(self):
        self.board.create_dwarf()
        self.board.create_gold()

    def game_action(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit()

            pressed = pygame.key.get_pressed()
            self.board.get_dwarf().move_dwarf(pressed, self.board)
            self.board.empty_board()

            self.board.draw_dwarf()
            for i in range(3):
                self.board.get_dwarf().catch_item(self.board.get_gold_items()[i])
                if (self.board.get_gold_items()[i].is_visible()):
                    self.board.draw_gold(i)

            time.sleep(0.004)
            pygame.display.update()

if __name__ == '__main__':
    interface = Interface()
    interface.set_up_screen(600, 600)
    interface.set_board()
    interface.create_all_elements()
    interface.game_action()