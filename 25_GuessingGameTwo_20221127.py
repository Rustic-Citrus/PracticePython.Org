import random

guess = 50
guess_min = 1
guess_max = 100
ongoing = True
total_guesses = 0

print('Playing guessing game...')
print('Think of a number between 1 and 100.')
next_step = input('Press any key to continue. ')
while ongoing == True:
    total_guesses += 1
    win = input(f'Press Y if your number was {guess}. ')
    if win.upper() == 'Y':
        print('Congrats to me!')
        print(f'I just guessed your number in {total_guesses} guesses!')
        ongoing = False
    
    else:
        responded = False
        while responded == False:
            error = input('Was my guess too HIGH or too LOW? \
(Type HIGH or LOW) ')
            if error.upper() == 'HIGH':
                guess_max = guess - 1
                responded = True

            elif error.upper() == 'LOW':
                guess_min = guess + 1
                responded = True

            else:
                print('ERROR: Please type HIGH or LOW.')

        guess = random.randint(guess_min, guess_max)

print('Thank you for playing!')
print('Ending game...')
