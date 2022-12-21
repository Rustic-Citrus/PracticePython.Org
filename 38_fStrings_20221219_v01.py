# For this problem, the instructions said that the Character Input problem 
# should be rewritten using f-strings. However, I already implemented 
# f-strings into the first version of my solution to the Character Input 
# problem, making the current iteration of this exercise redundant.

# As an alternative exercise, this script showcases f-strings by taking a date 
# of birth in ISO format and outputting the day of the week associated with 
# that date.

from datetime import date

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("""The ISO format for writing dates is YYYY-MM-DD.
For example, the date February 4 1957 would be written as 1957-02-04.""")
request = input("Type a date: ")

try:
    birthdate = date.fromisoformat(request)
    birthdate_weekday = weekdays[birthdate.isoweekday()-1]
    if birthdate.year < 1582:
        print("The date you inserted was before the adoption of the Gregorian calendar in 1582; therefore, the weekday is not the day of the week that those living at the time would have recognised.")
        print(f"Nevertheless, {birthdate.strftime('%d %B %Y')} would have been a {birthdate_weekday}.")

    else:
        print(f"{birthdate.strftime('%d %B %Y')} was a {birthdate_weekday}.")

except ValueError:
    print("ERROR: Invalid date.")
    print("Make sure to use the ISO format of YYYY-MM-DD.")
