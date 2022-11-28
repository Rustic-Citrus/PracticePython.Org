import random

def element_search(list, num):
    if num in list:
        return True
    else:
        return False

def fix_list(list):
    new_list = []
    list = list.split(',')
    for n in list:
        new_list.append(int(n.strip()))

    new_list.sort()
    return new_list
        
def generate_random_list():
    length = random.randint(10, 100)
    list = [random.randint(0, 100) for n in range(length)]
    return list

choice = int(input('Type an integer from 0 to 99. This program will \
tell you if it appeared in a randomly-generated list. '))
if element_search(generate_random_list(), choice) == True:
    print(f'{choice} was in the list.')
else:
    print(f'{choice} was not in the list.')
    