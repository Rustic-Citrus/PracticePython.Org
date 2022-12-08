# Below is the culmination of two other scripts in this folder, 'PickWord' and 
# 'GuessLetters', to form a complete, playable game of Hangman. 

import hangman_ascii
import random

def get_word():
    """Returns a random word from 'sowpods.txt'."""
    with open('sowpods.txt') as f:
        words = f.readlines()

    words = [word.strip('\n') for word in words]
    i = random.randint(0, len(words)-1)
    return words[i]

def get_progress():
    """Checks how many of the letters in the word have been guessed and
    returns a string where the unguessed letters are replaced with 
    underscores."""
    progress = ['_' for n in list(word)]
    for i in range(len(word)):
        if word[i] in guesses:
            progress[i] = word[i]

        else:
            progress[i] = '_'

    return ' '.join(progress)

def is_victory():
    """Checks if there are still any unguessed letters. If there are, 
    is_victory() returns False. If not, it returns True."""
    if '_' not in get_progress():
        return True
    
    else:
        return False

def is_defeat():
    """Checks if the player has any lives remaining. If the player has no 
    lives left, is_defeat() returns True. Otherwise, it returns False."""
    if lives == 0:
        return True

    else:
        return False

def play_again():
    """Asks the user if they would like to play again. Returns True if the 
    user presses 'Y'; otherwise, returns False."""
    x = input('Press Y to play again: ')
    if x.upper() == 'Y':
        return True

    else:
        return False

ongoing = True
guesses = []
lives = 6
word = get_word()

print('Welcome to Hangman!')

# Below is the loop that keeps the game going as long as the variable ongoing 
# is assigned to True.

while ongoing:

    # The loop begins by displaying the player's progress so far and then asks 
    # the user to type in a letter.

    print(get_progress())
    new_guess = input('Guess a letter: ')

    # Once the user has typed in a letter, it is then defined as either 
    # correct, a repeated guess or incorrect.

    if new_guess.upper() in word and new_guess.upper() not in guesses:
        print('Correct!')
        guesses.append(new_guess.upper())

    elif new_guess.upper() in word and new_guess.upper() in guesses:
        print('You already guessed that letter.')

    else:
        print('Incorrect!')
        guesses.append(new_guess.upper())
        lives -= 1

    # Next, it is determined whether the user has won the game, lost the game 
    # or neither. 
    
    # If the user has won or lost the game, the user is asked 
    # whether they would like to play again. If they say yes, the variables 
    # are reassigned to their original values and a new random word is 
    # generated. If they say no, the user is thanked for playing and the loop 
    # breaks.

    if is_victory():
        print('Congratulations!')
        print(f'The word was {word}.')
        if not play_again():
            print('Thank you for playing!')
            ongoing = False

        else:
            guesses = []
            lives = 6
            word = get_word()

    elif is_defeat():
        print(hangman_ascii.lives[0])
        print('You ran out of lives!')
        print(f'The word was {word}.')
        if not play_again():
            print('Thank you for playing!')
            ongoing = False

        else:
            guesses = []
            lives = 6
            word = get_word()
    
    # If the game is ongoing, then the user is told how many lives they have 
    # left and a visual representation of their situation is shown in the form 
    # of a hangman image.

    elif not is_victory() and not is_defeat():
        for n in hangman_ascii.lives:
            if n == lives and lives > 1:
                print(hangman_ascii.lives[n])
                print(f'You have {lives} lives left.')

            elif n == lives and lives == 1:
                print(hangman_ascii.lives[n])
                print(f'You have {lives} life left.')

        print(f'You have guessed: {guesses}.')
