from bokeh.plotting import figure, show, output_file
import json

with open("birthdays_months.json", "r") as f:
    db = json.load(f)

output_file("birthday_plots.html")
x_categories = [
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
x = list(db.keys())
y = list(db.values())
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)
