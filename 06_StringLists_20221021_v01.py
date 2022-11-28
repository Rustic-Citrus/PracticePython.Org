word = input("Type in a single word: ")
if word.lower()[::-1] == word.lower():
	print("It's a palindrome!")

else:
	print("It's not a palindrome.")
