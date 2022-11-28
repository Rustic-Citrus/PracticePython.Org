import random

n = random.randint(1, 9)
continue_game = True
while continue_game == True:
	guess = int(input("Guess a number between 1 and 9: "))
	if guess == n:
		print("Congratulations! You correctly guessed the number!")
		play_again = input("Press Y to play again. ")
		if play_again.lower() != "y":
			continue_game = False
			
		elif play_again.lower() == "y":
			n = random.randint(1, 9)

	elif guess > n:
		print("Not quite! Your guess was greater than the answer.")
		continue_playing = input("Press Y to try again. ")
		if continue_playing.lower() != "y":
			continue_game = False

	elif guess < n:
		print("Not quite! Your guess was less than the answer.")
		continue_playing = input("Press Y to try again. ")
		if continue_playing.lower() != "y":
			continue_game = False

	elif guess < 1 or guess > 9:
		print("Remember, the number has to be between 1 and 9!")
		continue_playing = input("Press Y to try again. ")
		if continue_playing.lower() != "y":
			continue_game = False

print("End of guessing game. Thanks for playing!")
