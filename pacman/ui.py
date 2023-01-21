def ui_print(game_map):
    for row in game_map:
        for column in row:
            print(column, end='')
        print('')
    print('')
