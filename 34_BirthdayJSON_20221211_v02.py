# This is a short script that does more or less the same thing as 
# BirthdayDictionaries, except that it takes the data from a JSON file instead 
# of a dictionary within the script. 

# On my first reading of the problem on PracticePython.org, I had assumed that 
# the focus of the activity was demonstrating an understanding of reading a 
# JSON file in Python. After having completed the activity and having moved on 
# to the next, I decided to reread the activity. That's when I noticed that 
# the focus of the activity was not just to demonstrate an understanding of 
# reading JSON files, but also of writing to JSON files. Therefore, in this 
# second version of the solution, I focus more on enabling the user to write 
# new information to birthdays.json.

# For the sake of posterity, I have included the lines of code that I used to 
# write the dictionary to a JSON file below.

import json

# birthdays = {
#     'Albert Einstein': '1879-03-14',
#     'Benjamin Franklin': '1706-01-17',
#     'Ada Lovelace': '1815-12-10'
# }

# with open('birthdays.json', 'w') as f:
#     json.dump(birthdays, f)

ongoing = True
with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

print('')
print('BIRTHDAYS OF FAMOUS SCIENTISTS')
while ongoing:
    try:
        print('')
        for n in birthdays.keys():
            print(n)
        
        print('')
        choice = int(input('''Press 1 to select a current scientist on the\
 list.
Press 2 to add a new scientist to the list. '''))
        print('')

        if choice == 1:
            selection = input('Choose the scientist whose birthday you would \
like to know: ')
            try:
                print(f"{selection.upper()}'S BIRTHDAY: {birthdays[selection.title()]}")

            except KeyError:
                print('ERROR: Invalid name input.')

        if choice == 2:
            scientist_name = input('Type the name of the scientist: ').title()
            print('The date of birth should be in the format YYYY-MM-DD.')
            scientist_dob = input('Type the date of birth of the scientist: ')
            birthdays[scientist_name] = scientist_dob

        elif choice != 1 and choice != 2:
            print('ERROR: Input was neither 1 nor 2.')

    except:
        print('ERROR: Input is not a number.')

    is_ongoing = input('Press Y to continue or any other letter to exit \
and write additional scientists to the JSON file. ')
    if is_ongoing.upper() != 'Y':
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
        print('END')
        ongoing = False
