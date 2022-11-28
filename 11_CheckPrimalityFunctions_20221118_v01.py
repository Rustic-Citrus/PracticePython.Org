repeat = True
end = 'Ending program...'
def check_prime(n):
    is_prime = True
    for i in range(2, 10):
        if n % i == 0:
            is_prime = False
            break

        else:
            is_prime = True
    
    if is_prime == True:
        print(affirmative)

    elif is_prime == False:
        print(negative)

while repeat == True:
    try:
        n = int(input('Type any integer: '))
        affirmative = f'{n} is a prime number.'
        negative = f'{n} is not a prime number.'
        if n not in [1, 3, 5, 7]:
            check_prime(n)

        elif n in [1, 3, 5, 7]:
            print(affirmative)
        
        decision = input(
            'Press Y to choose another number. Press any other key to end the program. ')
        if decision.lower() != 'y':
            print(end)
            repeat = False

    except ValueError:
        print('ERROR: Please type an integer.')
