import random

print("~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~")

choice = int(input("Choose a number from 0 to 100: "))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if (choice > 100) or (choice < 0):

	raise ValueError("Choice must be equal to or greater than 0 and equal to or less than 100.")

else:

	ls = [random.randint(0, 100) for n in range(10)]

	print(f"Randomly generated list of ten numbers from 0 to 100:")
	print(ls)

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	nums = [n for n in ls if n < choice]

	# count = 0
	# for n in ls:
	# 	if n < choice:
	# 		count += 1

	print(f"There are {len(nums)} numbers less than {choice} in the list.")

	if len(nums) != 0:

		print(nums)

	print("~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~")
