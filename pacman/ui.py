def ui_print(game_map):
    for row in game_map:
        for column in row:
            print(column, end='')
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
