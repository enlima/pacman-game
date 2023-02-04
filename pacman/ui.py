# ASCII arts from https://www.asciiart.eu/video-games/pacman
ui_pacman = [
    " .--. ",
    "/ _.-'",
    "\\  '-.",
    " '--' "
]

ui_ghost = [
    " .-.  ",
    "| OO| ",
    "|   | ",
    "'^^^' "
]

ui_pill = [
    "      ",
    " .-.  ",
    " '-'  ",
    "      "
]

ui_empty = [
    "      ",
    "      ",
    "      ",
    "      "
]

ui_wall = [
    "......",
    "......",
    "......",
    "......"
]


def ui_print(game_map):
    for row in game_map:
        for piece in range(4):
            for column in row:
                match column:
                    case '.':
                        print(ui_empty[piece], end='')
                    case '-' | '|':
                        print(ui_wall[piece], end='')
                    case '@':
                        print(ui_pacman[piece], end='')
                    case 'G':
                        print(ui_ghost[piece], end='')
                    case 'P':
                        print(ui_pill[piece], end='')
            print('')


def ui_key():
    return input()


def is_valid_key(key):
    if key.lower() in ['a', 'w', 'd', 's']:
        return True

    return False


def ui_msg_invalid_key():
    print("====================")
    print("=   Invalid key!   =")
    print("=      Press:      =")
    print("= A-left | D-right =")
    print("= W-up   | S-down  =")
    print("====================")


def ui_msg_victory():
    print("====================")
    print("= @@ YOU WON!!! @@ =")
    print("====================")


def ui_msg_game_over():
    print("====================")
    print("= GG Game Over! GG =")
    print("====================")
