import datetime

# Parsing user data

print("Welcome!")
print("This program gives you some information about your life.")
print("All you have to do is put in a name and an age.")

name = input("What is your name? ")
print(f"Your name is {name}.")

if type(name) != str:
	print("What an unusual name!")

try:
	age = int(input("How old are you? "))
	print(f"You are {age} years old.")
except:
	raise TypeError("Woops! Your age must be an integer.")

# Estimating when the user was born

today = datetime.date.today()
year_of_birth = today.year - int(age)

# Estimating future life events of user

hundredth_birthday = year_of_birth + 100
retirement_year = year_of_birth + 65

# Info about birth

if year_of_birth > today.year:
	print(f"Hmmm, it seems you haven't even been born yet, {name}!")
	raise ValueError("Age must be equal to or greater than zero")
elif year_of_birth == today.year:
	print(f"Welcome to the world, {name}!")
else:
	print(f"{name}, I'm guessing you were born in either {year_of_birth - 1} or {year_of_birth}.")

# Info about retirement

if retirement_year < today.year:
	print(f"I hope that you're enjoying your retirement!")
elif retirement_year == today.year:
	print(f"Assuming that you plan on retiring at 65, you will be retiring this year!")
else:
	print(f"Assuming that you retire when you are 65, then you will retire in {retirement_year}.")

# Info about hundredth birthday

if hundredth_birthday < today.year:
	print(f"{name}, congratulations on being over a hundred years old!")
elif hundredth_birthday == today.year:
	print(f"Happy birthday, {name}! Either last year was or this year is your 100th birthday!")
else:
	print(f"Your 100th birthday will be in either {hundredth_birthday - 1} or {hundredth_birthday}.")
