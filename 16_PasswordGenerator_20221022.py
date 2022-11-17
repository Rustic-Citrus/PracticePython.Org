import string
import random

password_length = int(input("Type the number of characters for your password. "))

numbers = input("Press Y to include numbers in your password. ")

if numbers.lower() == "y":

	numbers = True

else:

	numbers = False

punctuation = input("Press Y to include punctuation in your password. ")

if punctuation.lower() == "y":

	punctuation = True

else:

	punctuation = False

password = ""

categories = [string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

for i in range(password_length):

	if punctuation == True and numbers == True:

		x = categories[random.randint(0, len(categories) - 1)]

	elif punctuation == True and numbers == False:

		x = categories[random.randint(1, len(categories) - 1)]

	elif punctuation == False and numbers == True:

		x = categories[random.randint(0, len(categories) - 2)]

	else:

		x = categories[random.randint(1, len(categories) - 2)]

	n = x[random.randint(0, len(x) - 1)]

	password = password + n

print(f"Generated password: {password}")
