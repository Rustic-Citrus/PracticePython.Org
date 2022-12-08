# This is a short script that demonstrates the logic behind the classic game 
# of Hangman. It is one of three scripts in this folder that together 
# represent the complete game of Hangman.

ongoing = True
word = 'SERENDIPITY'
guesses = []
lives = 6

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
    # or neither. If the user has won or lost the game, the ongoing variable 
    # is assigned to False and the loop ends.

    if is_victory():
        print('Congratulations!')
        print(f'The word was {word}.')
        ongoing = False

    elif is_defeat():
        print('You ran out of lives!')
        print(f'The word was {word}.')
        ongoing = False
    
    elif not is_victory() and not is_defeat():
        if lives > 1:
            print(f'You have {lives} lives left.')

        elif lives == 1:
            print(f'You have {lives} life left.')
