# This is a short script that presents an example of a dictionary containing 
# the birthdays of three historical figures, as well as a means of the user 
# visualising the data contained within the dictionary through the command 
# line.

import datetime

ongoing = True
birthdays = {
    'Albert Einstein': datetime.datetime(1879, 3, 14),
    'Benjamin Franklin': datetime.datetime(1706, 1, 17),
    'Ada Lovelace': datetime.datetime(1815, 12, 10)
}
for n in birthdays.keys():
    print(n)

while ongoing:
    choice = input('Choose the person whose birthday you would like to know: ')
    try:
        print(birthdays[choice.title()].date())

    except KeyError:
        print('ERROR: Invalid name input.')

    is_ongoing = input('Press Y to choose another person. ')
    if is_ongoing.upper() != 'Y':
        ongoing = False
