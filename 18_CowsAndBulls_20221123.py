import random

in_progress = True
guesses = 0

def generate_number():
    global num
    num = str(random.randint(1000, 10000))

generate_number()
while in_progress == True:
    bulls = 0
    cows = 0
    user_guess = input('Guess a number between 1000 and 9999: ')
    if user_guess == num:
        guesses += 1
        print('Congratulations! You guessed the number!')
        print(f'You guessed the number in {guesses} tries.')
        in_progress = False

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
