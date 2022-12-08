import random

def get_word():
    with open('sowpods.txt') as f:
        lines = f.readlines()

    lines = [word.strip('\n') for word in lines]
    i = random.randint(0, len(lines)-1)
    return lines[i]

print(get_word())
