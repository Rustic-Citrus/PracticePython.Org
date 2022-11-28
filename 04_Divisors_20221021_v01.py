import warnings

choice = int(input("Choose a number: "))
ls = []
x = choice
while x > 0:
	if choice % x == 0:
		ls.append(x)

	x -= 1

def get_divisors():
	if len(ls) > 2:
		print(f"The following {len(ls)} numbers are divisors of {choice}:")
		for n in ls:
			print(n)

	elif len(ls) == 2:
		print(f"{choice} is a prime number.")

	elif len(ls) == 1:
		print("1 has only one divisor: itself.")

	elif len(ls) == 0:
		print("0 has no divisors.")


if len(ls) > 20:
	warnings.warn("There are more than 20 divisors.")
	go_ahead = input("Press Y to continue anyway. ")
	if go_ahead == "y" or go_ahead == "Y":
		get_divisors()

	else:
		print("Ended program without showing divisors.")

else:
	get_divisors()
