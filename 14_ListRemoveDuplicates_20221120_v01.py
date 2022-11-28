def remove_duplicates_one(lst):
    """Takes a list, converts it into a set, then back into a list and
returns the result."""
    return list(set(lst))

def remove_duplicates_two(lst):
    """Takes a list, loops through it and then adds any non-duplicate 
values to a new list. The new list is then returned."""
    n = 0
    new_lst = []
    while n < len(lst):
        if lst[n] not in new_lst:
            new_lst.append(lst[n])
        n += 1
    return new_lst

print('Make sure your list is comma-separated; i.e. a, b, c...')
user_lst = input('Paste your list here: ')
user_lst = user_lst.split(',')
user_lst = [i.strip() for i in user_lst]
print(f'Set Method: {remove_duplicates_one(user_lst)}')
print(f'Loop Method: {remove_duplicates_two(user_lst)}')
