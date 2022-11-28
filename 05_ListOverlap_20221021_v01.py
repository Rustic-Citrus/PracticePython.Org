import random

print("Generating two sets of random numbers from 0 to 100...")
set1 = {random.randint(0, 100) for n in range(25)}
print(f"SET 1: {set1}")
set2 = {random.randint(0, 100) for n in range(25)}
print(f"SET 2: {set2}")
print("Checking both sets from similarities...")
similarities = set1.intersection(set2)
def get_similarities():
	for n in similarities:
		print(n)

if len(similarities) > 1:
	print(f"There were {len(similarities)} numbers in common between the two sets:")
	get_similarities()

elif len(similarities) == 1:
	print("There was one number in common between the two sets:")
	get_similarities()

elif len(similarities) == 0:
	print("There were no numbers in common between the two sets.")
