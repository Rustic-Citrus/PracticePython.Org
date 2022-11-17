response = "y"

print("Welcome!")
print("""This program lets you test two values
to see if they are multiples of one another.""")

while response.lower() == "y":
	try:
		number1 = int(input("Choose your 1st number: "))
		number2 = int(input("Choose your 2nd number: "))

	except:
		print("Woops! Looks like you didn't type a number.")

	# Even numbers.
	if (number1 != number2) and (number1 % 2 == 0) and (number1 % 4 != 0) and (number1 % number2 == 0):
		print(f"{number1} is an even number, and is divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	elif (number1 != number2) and (number1 % 2 == 0) and (number1 % 4 != 0) and (number1 % number2 != 0):
		print(f"{number1} is an even number, but is not divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	# Odd numbers.
	elif (number1 != number2) and (number1 % 2 == 1) and (number1 % number2 == 0):
		print(f"{number1} is an odd number, and is divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	elif (number1 != number2) and (number1 % 2 == 1) and (number1 % number2 != 0):
		print(f"{number1} is an odd number, and is not divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	# Multiples of 4.
	elif (number1 != number2) and (number1 % 2 == 0) and (number1 % 4 == 0) and (number1 % number2 != 0):
		print(f"{number1} is an even number, a multiple of 4, but is not divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	elif (number1 != number2) and (number1 % 2 == 0) and (number1 % 4 == 0) and (number1 % number2 == 0):
		print(f"{number1} is an even number, a multiple of 4, and is divisible by {number2}.")
		response = input("Press Y to choose another number. ")

	# Equal numbers.
	elif (number1 == number2) and (number1 % 2 == 0):
		print(f"Both numbers are equal, and they are even.")
		response = input("Press Y to choose another number. ")

	elif (number1 == number2) and (number1 % 2 == 1):
		print(f"Both numbers are equal, and they are odd.")
		response = input("Press Y to choose another number. ")

