board = [
    [' --- ', ' --- ', ' --- '],
    ['|   |', '|   |', '|   |'],
    [' --- ', ' --- ', ' --- '],
    ['|   |', '|   |', '|   |'],
    [' --- ', ' --- ', ' --- '],
    ['|   |', '|   |', '|   |'],
    [' --- ', ' --- ', ' --- ']
]
ongoing = True
counter = 0

def get_board():
    """Prints the board in its current state."""
    for row in board:
        print(row[0] + row[1] + row[2])

def parse_coord(coord):
    """Takes the coordinates supplied by the user and converts them 
into a tuple of two zero-indexed integers representing the x and y 
coordinates of the board."""
    clean_coord = coord.strip()
    clean_coord = clean_coord.split(',')
    x, y = clean_coord
    return (int(x)+int(x)-1, int(y)-1)

def set_position(x, y, player):
    """Takes the coordinates and the player number as arguments and 
either successfully updates the game board and returns True or fails 
and returns False."""
    symbol = ''
    if player == 1:
        symbol = 'X'

    elif player == 2:
        symbol = 'O'

    try:
        if board[x][y][2] == ' ':
            cell = list(board[x][y])
            cell[2] = symbol
            board[x][y] = ''.join(cell)
            return True
        
        elif board[x][y][2] == ' ':
            return False

    except IndexError:
        return False

def get_winner():
    """Checks the matrix horizontally, vertically and diagonally to 
    see whether a player has won."""
    # Checks horizontally.
    player_one_symbol, player_two_symbol = ['X', 'O']
    player_one_count, player_two_count = [0, 0]
    for x in range(1, 6, 2):
        for y in range(0, 3):
            if board[x][y][2] == player_one_symbol:
                player_one_count += 1
                player_two_count = 0
            
            elif board[x][y][2] == player_two_symbol:
                player_two_count += 1
                player_one_count = 0

            elif board[x][y][2] == ' ':
                player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    # Checks vertically.
    counter = 1
    player_one_count, player_two_count = [0, 0]
    for y in range(0, 3):
        for x in range(1, 6, 2):
            if board[x][y][2] == player_one_symbol:
                player_one_count += 1
                player_two_count = 0
            
            elif board[x][y][2] == player_two_symbol:
                player_two_count += 1
                player_one_count = 0

            elif board[x][y][2] == ' ':
                player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    # Checks diagonally from top-left to bottom-right.
    player_one_count, player_two_count = [0, 0]
    for (x, y) in zip(range(1, 6, 2), range(3)):
        if board[x][y][2] == player_one_symbol:
            player_one_count += 1
            player_two_count = 0
        
        elif board[x][y][2] == player_two_symbol:
            player_one_count = 0
            player_two_count += 1

        elif board[x][y][2] == ' ':
            player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    # Checks diagonally from top-right to bottom-left.
    player_one_count, player_two_count = [0, 0]
    for (x, y) in zip(range(5, 0, -2), range(3)):
        if board[x][y][2] == player_one_symbol:
            player_one_count += 1
            player_two_count = 0
        
        elif board[x][y][2] == player_two_symbol:
            player_one_count = 0
            player_two_count += 1

        elif board[x][y][2] == ' ':
            player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    return (False, 0)

while ongoing:
    for player in range(1, 3):
        if counter == 9:
            print("It's a draw!")
            ongoing = False
            get_board()
            break

        get_board()
        print(f'Player {player},')
        print(f'Type the coordinates of the cell where you would like \
to place your mark.')
        print('For example, to select the cell in the first row and \
first column, type 1, 1')
        coord = input('Coordinates: ')
        x, y = parse_coord(coord)
        if set_position(x, y, player):
            set_position(x, y, player)

        elif not set_position(x, y, player):
            while not set_position(x, y, player):
                print('ERROR: Invalid coordinates.')
                print(f'Player {player},')
                print(f'Type the coordinates of a cell where you would \
like to place your mark.')
                print('For example, to select the cell in the first row \
and first column, type 1, 1')
                coord = input('Coordinates: ')
                x, y = parse_coord(coord)
                if set_position(x, y, player):
                    set_position(x, y, player)
                    break
    
        if get_winner() == (True, 1):
            print('Player One wins.')
            ongoing = False
            get_board()
            break

        if get_winner() == (True, 2):
            print('Player Two wins.')
            ongoing = False
            get_board()
            break

        counter += 1
