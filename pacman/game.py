from pacman.ui import ui_print

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


def play(game_map, key):
    if is_valid_key(key):
        next_x_pos, next_y_pos = calculate_next_position(game_map, key)

        if is_within_borders(game_map, next_x_pos, next_y_pos) and not is_a_wall(game_map, next_x_pos, next_y_pos):
            if is_a_ghost(game_map, next_x_pos, next_y_pos):
                print("====================")
                print("= GG Game Over! GG =")
                print("====================")
            else:
                move_pacman(game_map, next_x_pos, next_y_pos)

        if not is_there_remaining_pills(game_map):
            print("====================")
            print("= @@ YOU WON!!! @@ =")
            print("=     CONGRATS     =")
            print("====================")


def is_valid_key(key):
    if key.lower() in ['a', 'w', 'd', 's']:
        return True

    print("Invalid key!")
    print("Press 'A' to move left, 'W' to move up, 'D' to move right or 'S' to move down.")

    return False


def calculate_next_position(game_map, key):
    pacman_x, pacman_y = find_pacman(game_map)
    next_x_pos = pacman_x
    next_y_pos = pacman_y

    match key.lower():
        case 'a':
            next_y_pos = pacman_y - 1
        case 'd':
            next_y_pos = pacman_y + 1
        case 'w':
            next_x_pos = pacman_x - 1
        case 's':
            next_x_pos = pacman_x + 1

    return next_x_pos, next_y_pos


def find_pacman(game_map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y


def is_within_borders(game_map, next_x_pos, next_y_pos):
    number_of_rows = len(game_map)
    is_valid_x = 0 <= next_x_pos < number_of_rows

    number_of_columns = len(game_map[0])
    is_valid_y = 0 <= next_y_pos < number_of_columns

    return is_valid_x and is_valid_y


def is_a_wall(game_map, next_x_pos, next_y_pos):
    return game_map[next_x_pos][next_y_pos] == '|' or game_map[next_x_pos][next_y_pos] == '-'


def is_a_ghost(game_map, next_x_pos, next_y_pos):
    return game_map[next_x_pos][next_y_pos] == 'G'


def is_there_remaining_pills(game_map):
    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == 'P':
                return True

    return False


def move_pacman(game_map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(game_map)

    # clears the position where pacman was
    game_map[pacman_x] = game_map[pacman_x][0:pacman_y] + '.' + game_map[pacman_x][pacman_y + 1:]
    # moves pacman to his new position
    game_map[next_pacman_x] = game_map[next_pacman_x][0:next_pacman_y] + '@' + game_map[next_pacman_x][
                                                                               next_pacman_y + 1:]


ui_print(game_map)
play(game_map, 'x')
ui_print(game_map)
play(game_map, 'w')
ui_print(game_map)
play(game_map, 'a')
ui_print(game_map)
