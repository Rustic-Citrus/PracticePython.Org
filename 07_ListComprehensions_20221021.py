import random

ls = [random.randint(0, 10) for n in range(10)]
print(ls)
evens = [n for n in ls if n % 2 == 0]
print(evens)
