from utils.json_parser import JsonParser
from game_board.interface_v2 import Interface

config = JsonParser.parse_configuration()


if __name__ == '__main__':
    interface = Interface()
    interface.set_up_screen(config["screen_size"], config["screen_size"])
    interface.set_board()
    interface.create_all_elements(config["count_of_gold"], config["count_of_kobolds"])
    interface.set_game_logic()
    interface.game_action()