# In my solution to the first problem, I used the datetime module. Thus, this 
# particular exercise was made redundant. For the sake of practice, I have 
# taken the opportunity to polish up the script that I wrote for the first 
# problem.

from datetime import datetime
import math

name = input("Type your name: ")
date_of_birth = datetime.fromisoformat(input("Type your birthday in ISO format (YYYY-MM-DD): "))
date_today = datetime.now()
age = date_today - date_of_birth
print(f"""{name}, you were born about {date_today.year - date_of_birth.year} years and {math.floor(age.days - ((date_today.year - date_of_birth.year) * 365.25))} days ago, on {date_of_birth.strftime('%d %B %Y')}.
In {date_of_birth.year + 18}, you became an adult.
If you intend to retire when you're 65 years old, then you should retire in {date_of_birth.year + 65}.""")
