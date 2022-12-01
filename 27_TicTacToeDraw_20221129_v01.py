game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
ongoing = True

def parse_coord(coord):
    """Takes the coordinates supplied by the user and converts them 
into a tuple of two zero-indexed integers representing the x and y 
coordinates of the board."""
    clean_coord = coord.strip()
    clean_coord = clean_coord.split(',')
    x, y = clean_coord
    return (int(x) - 1, int(y) - 1)

def set_coord(x, y, player):
    """Takes the coordinates and the player number as arguments and 
either successfully updates the game board and returns True or fails 
and returns False."""

    try:
        if game[x][y] == 0:
            game[x][y] = player
            return True
        
        elif game[x][y] != 0:
            return False

    except IndexError:
        return False

for l in game:
    print(l)

for possible_moves in range(0, 9):
    for player in range(1, 3):
        print(f'Player {player},')
        print(f'Type the coordinates of a cell where you would like \
to place a {player}.')
        print('For example, to select the cell in the first row and \
first column, type 1, 1')
        coord = input('Coordinates: ')
        x, y = parse_coord(coord)
        if set_coord(x, y, player):
            set_coord(x, y, player)

        elif not set_coord(x, y, player):
            while not set_coord(x, y, player):
                print('ERROR: Invalid coordinates.')
                print(f'Player {player},')
                print(f'Type the coordinates of a cell where you would \
like to place a {player}.')
                print('For example, to select the cell in the first row \
and first column, type 1, 1')
                coord = input('Coordinates: ')
                x, y = parse_coord(coord)
                if set_coord(x, y, player):
                    set_coord(x, y, player)
                    break

        for l in game:
            print(l)
