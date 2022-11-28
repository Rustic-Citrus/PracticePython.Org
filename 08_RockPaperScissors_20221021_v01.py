import random

name = input("Type your name: ")
moves = ["rock", "paper", "scissors"]
wins = 0
losses = 0
playing = True
while playing == True:
	player_move = input("Rock, paper or scissors? ")
	ai_move = moves[random.randint(0, 2)]
	if player_move.lower() == ai_move: # Player and Computer make the same move.
		print(f"Both players chose {player_move}. It's a draw!")

	elif player_move.lower() == "rock" and ai_move == "paper": # Player plays "rock", Computer plays "paper".
		print(f"{name} chose Rock and the computer chose Paper. Computer wins!")
		losses += 1

	elif player_move.lower() == "rock" and ai_move == "scissors": # Player plays "rock", Computer plays "scissors".
		print(f"{name} chose Rock and the computer chose Scissors. {name} wins!")
		wins += 1

	elif player_move.lower() == "paper" and ai_move == "rock": # Player plays "paper", Computer plays "rock".
		print(f"{name} chose Paper and the computer chose Rock. {name} wins!")
		wins += 1

	elif player_move.lower() == "paper" and ai_move == "scissors": # Player plays "paper", Computer plays "scissors".
		print(f"{name} chose Paper and the computer chose Scissors. Computer wins!")
		losses += 1

	elif player_move.lower() == "scissors" and ai_move == "rock": # Player plays "scissors", Computer plays "rock".
		print(f"{name} chose Scissors and the computer chose Rock. Computer wins!")
		losses += 1

	elif player_move.lower() == "scissors" and ai_move == "paper": # Player plays "scissors", Computer plays "paper".
		print(f"{name} chose Scissors and the computer chose Paper. {name} wins!")
		wins += 1

	print("Current score:")
	print(f"{name}: {wins}")
	print(f"Computer: {losses}")
	continue_game = input("Press Y to continue playing. ")
	if continue_game.lower() == "y":
		playing = True

	else:
		playing = False

print("End of game. Thanks for playing!")
