def draw_board(rows, columns):
    top = ' --- '
    sides = '|   |'
    for n in range(rows):
        print(top * columns)
        print(sides * columns)
    print(top * columns)

print('Drawing a game board...')
rows = int(input('Type the number of rows for your board: '))
columns = int(input('Type the number of columns for your board: '))
draw_board(rows, columns)
print('Done!')
