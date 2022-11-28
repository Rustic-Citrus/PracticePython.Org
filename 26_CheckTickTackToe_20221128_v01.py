import random

game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
moves = {
    1: 5,
    2: 4
    }

def set_move(player):
    """Sets a random coordinate in the matrix to 1 or 2 if there is
    a 0 at the coordinate."""
    success = False
    while (success == False) and (moves[player] > 0):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if game[x][y] == 0:
            game[x][y] = player
            success = True
            moves[player] -= 1

def get_winner():
    """Checks the matrix horizontally, vertically and diagonally to 
    see whether a player has won."""
    # Checks horizontally.
    player_one_count, player_two_count = [0, 0]
    for x in range(0, 3):
        for y in range(0, 3):
            if game[x][y] == 1:
                player_one_count += 1
                player_two_count = 0
            
            elif game[x][y] == 2:
                player_two_count += 1
                player_one_count = 0

            elif game[x][y] == 0:
                player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    # Checks vertically.
    counter = 0
    player_one_count, player_two_count = [0, 0]
    for y in range(0, 3):
        for x in range(0, 3):
            if game[x][y] == 1:
                player_one_count += 1
                player_two_count = 0
            
            elif game[x][y] == 2:
                player_two_count += 1
                player_one_count = 0

            elif game[x][y] == 0:
                player_one_count, player_two_count = [0, 0]

        if player_one_count == 3:
            return (True, 1)

        elif player_two_count == 3:
            return (True, 2)

    # Checks diagonally.
    player_one_count, player_two_count = [0, 0]
    for (x, y) in zip(range(2, -1, -1), range(3)):
        if game[x][y] == 1:
            player_one_count += 1
            player_two_count = 0
        
        elif game[x][y] == 2:
            player_one_count = 0
            player_two_count += 1

        elif game[x][y] == 0:
            player_one_count, player_two_count = [0, 0]

    if player_one_count == 3:
        return (True, 1)

    elif player_two_count == 3:
        return (True, 2)

    return (False, 0)

for n in range(9):
    set_move(1)
    if get_winner() == (True, 1):
        print('Player One wins.')
        break
    set_move(2)
    if get_winner() == (True, 2):
        print('Player Two wins.')
        break

if get_winner() == (False, 0):
    print('Draw.')

print(game[0])
print(game[1])
print(game[2])
