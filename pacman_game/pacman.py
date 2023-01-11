from pacman_game.ui import ui_print

# @ -> pacman
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]


def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y


def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    # clears the position where pacman was
    map[pacman_x] = map[pacman_x][0:pacman_y] + '.' + map[pacman_x][pacman_y + 1:]
    # moves pacman to his new position
    map[next_pacman_x] = map[next_pacman_x][0:next_pacman_y] + '@' + map[next_pacman_x][next_pacman_y + 1:]


def play(map, key):
    if is_valid_key(key):
        next_x_pos, next_y_pos = calculate_next_position(map, key)
        move_pacman(map, next_x_pos, next_y_pos)


def is_valid_key(key):
    if key.lower() in ['a', 'w', 'd', 's']:
        return True

    print("Invalid key!")
    print("Press 'A' to move left, 'W' to move up, 'D' to move right or 'S' to move down.")

    return False


def calculate_next_position(map, key):
    pacman_x, pacman_y = find_pacman(map)
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


ui_print(map)
play(map, 'D')
ui_print(map)
play(map, 's')
ui_print(map)
play(map, 'x')
ui_print(map)
