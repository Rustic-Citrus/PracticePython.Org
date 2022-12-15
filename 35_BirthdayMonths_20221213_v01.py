# This is a simple script that takes a JSON file containing the dates of birth 
# of well-known scientists and presents how many of them were born in each 
# month.

import json
from collections import Counter

def monthnumbertostring(n):
    monthstrings = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return monthstrings[n-1]

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

for m, n in birthdays.items():
    birthdays[m] = monthnumbertostring(int(n[5:7]))

c = Counter(birthdays.values())
print(c)
