import random

class InvalidNumber(Exception): pass

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        number_of_guesses += 1
        if (guess < 1) or (guess > 9):
            raise InvalidNumber
        elif guess == number:
            break

    except InvalidNumber:
        print("ERROR: Number was less than 1 or greater than 9.")
        
print(f"You needed {number_of_guesses} guesses to guess the number {number}")
