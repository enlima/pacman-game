from pacman.game import play
from pacman.result_enum import Result
from pacman.ui import ui_print, ui_key, is_valid_key, ui_msg_invalid_key, ui_msg_game_over, ui_msg_victory

# @ -> pacman
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
game_map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

is_game_finished = False

while not is_game_finished:
    ui_print(game_map)

    key = ui_key()

    if not is_valid_key(key):
        ui_msg_invalid_key()
    else:
        match play(game_map, key):
            case Result.CONTINUE:
                continue
            case Result.VICTORY:
                ui_msg_victory()
                is_game_finished = True
            case Result.GAME_OVER:
                ui_msg_game_over()
                is_game_finished = True
