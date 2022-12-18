# For this exercise, the instructions say that I should refactor a few lines 
# of code that I had written for the Draw a Game Board exercise as a function. 
# However, I already wrote the Draw a Game Board exercise as a function. 
# Therefore, to make this exercise more meaningful for my specific case, I 
# decided to refactor as a function some lines of code that I frequently write 
# at the end of a while loop; namely, the lines of code that ask whether the 
# user would like to continue.

# Here I have more or less used the code that I wrote for the game Cows and 
# Bulls, but I have added in the ongoing function and created the EndGame 
# exception class. Although the result is a script with a few more lines of 
# code, the result is also more compact and compartmentalised. The while loop 
# where the gameplay takes place is less cluttered and more readable. Moreover,
# in the non-refactored script, the script will end abruptly when a 
# KeyboardInterrupt exception is raised; whereas the refactored script exits 
# cleanly. 

import random

class EndGame(Exception): pass

def ongoing():
    x = input('Press Y to continue, or any other key to exit. ')
    if x.upper() != 'Y':
        raise EndGame


def generate_number():
    global num
    num = str(random.randint(1000, 10000))


try:
    guesses = 0
    generate_number()
    while 1 > 0:
        bulls = 0
        cows = 0
        user_guess = input('Guess a number between 1000 and 9999: ')
        if user_guess == num:
            guesses += 1
            print('Congratulations! You guessed the number!')
            print(f'You guessed the number in {guesses} tries.')
            ongoing()

        else:
            for i in range(4):
                if user_guess[i] == num[i]:
                    bulls += 1
                
                elif user_guess[i] != num[i] and user_guess[i] in num:
                    cows += 1
            
            guesses += 1
            print(f'{bulls} bulls and {cows} cows.')
            print(f'{guesses} guesses so far.')
            print('Try again.')

except (EndGame, KeyboardInterrupt) as e:
    print('Ending game...')
    print('Thank you for playing!')
