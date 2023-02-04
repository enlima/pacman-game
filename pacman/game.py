import random

from pacman.result_enum import Result


def play(game_map, key):
    next_x_pos, next_y_pos = calculate_next_position(game_map, key)

    if is_within_borders(game_map, next_x_pos, next_y_pos) and not is_a_wall(game_map, next_x_pos, next_y_pos):
        if is_a_ghost(game_map, next_x_pos, next_y_pos):
            return Result.GAME_OVER
        else:
            move_pacman(game_map, next_x_pos, next_y_pos)

    if not is_there_remaining_pills(game_map):
        return Result.VICTORY

    return move_ghosts(game_map)


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


def is_a_pill(game_map, next_x_pos, next_y_pos):
    return game_map[next_x_pos][next_y_pos] == 'P'


def is_pacman(game_map, next_x_pos, next_y_pos):
    return game_map[next_x_pos][next_y_pos] == '@'


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


def move_ghosts(game_map):
    all_ghosts = find_all_ghosts(game_map)

    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_new_positions = [
            [ghost_x, ghost_y + 1],
            [ghost_x + 1, ghost_y],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y]
        ]

        random_number = random.randint(0, 3)
        next_ghost_x = possible_new_positions[random_number][0]
        next_ghost_y = possible_new_positions[random_number][1]

        if not is_within_borders(game_map, next_ghost_x, next_ghost_y):
            continue

        if is_a_wall(game_map, next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(game_map, next_ghost_x, next_ghost_y):
            continue

        if is_a_pill(game_map, next_ghost_x, next_ghost_y):
            continue

        if is_pacman(game_map, next_ghost_x, next_ghost_y):
            return Result.GAME_OVER

        # clears the position where ghost was
        game_map[ghost_x] = game_map[ghost_x][0:ghost_y] + '.' + game_map[ghost_x][ghost_y + 1:]
        # moves ghost to his new position
        game_map[next_ghost_x] = game_map[next_ghost_x][0:next_ghost_y] + 'G' + game_map[next_ghost_x][
                                                                                next_ghost_y + 1:]

    return Result.CONTINUE


def find_all_ghosts(game_map):
    all_ghosts_positions = []

    for x in range(len(game_map)):
        for y in range(len(game_map[x])):
            if game_map[x][y] == 'G':
                all_ghosts_positions.append([x, y])

    return all_ghosts_positions
