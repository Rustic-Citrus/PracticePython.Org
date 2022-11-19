repeat = True
def list_overlap(a, b):
    a = a.split(',')
    a = [x.strip() for x in a]
    b = b.split(',')
    b = [x.strip() for x in b]
    c = list(set([x for x in a if (x in a) and (x in b)]))
    return c

def get_repeat():
    if user_choice.lower() != 'y':
        global repeat
        repeat = False
        print('Ending program...')

user_choice = input('Press Y to use own lists or press any other key to \
see an example: ')
while repeat == True:
    if user_choice.lower() == 'y':
        print('Use commas to separate the list items.')
        print('Your list should look like this: x, y, z')
        a = input('Type or paste the first list: ')
        b = input('Type or paste the second list: ')
        print(f'List overlap: {list_overlap(a, b)}')
        user_choice = input('Press Y to use another set of lists. ')
        get_repeat()

    else:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        print(f'Example list A: {a}')
        print(f'Example list B: {b}')
        print(f'List overlap: {list_overlap(a, b)}')
        user_choice = input('Press Y to use your own list. ')
        get_repeat()
