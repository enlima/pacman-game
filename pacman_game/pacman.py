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


ui_print(map)
move_pacman(map, 3, 6)
ui_print(map)
