# This is a short script that does more or less the same thing as 
# BirthdayDictionaries, except that it takes the data from a JSON file instead 
# of a dictionary within the script. 

# Originally, the exercise asked that you convert the dictionary from the 
# previous exercise to a JSON file, and the read it to access the data. I 
# found that a little too simple, so I decided to research a dataset that was 
# in the JSON format, and use that instead. The one I chose was the 'World 
# University Rankings 2021' dataset, provided by the Matheus Gratz. I 
# downloaded it on 2022-12-11 from 
# https://www.kaggle.com/datasets/matheusgratz/world-university-rankings-2021?select=universities_ranking.json. It can be found in this repository as 
# 'universities_ranking.json'.

import json

ongoing = True
with open('universities_ranking.json', 'r') as f:
    university_rankings = json.load(f)

print('WORLD UNIVERSITY RANKINGS, 2021')
print('from The Times Higher Education')
print('')
print('TOP 10 UNIVERSITIES (2021):')
for n in range(11):
    for university in university_rankings:
        if n == university['ranking']:
            print(f"{n}. {university['title']}, {university['location']}")

print('')
print('TOP 10 UNIVERSITIES IN SOUTH AMERICA (2021):')
n = 0
for university in university_rankings:
    if university['location'] in [
        'Argentina',
        'Bolivia',
        'Brazil',
        'Chile',
        'Colombia',
        'Ecuador',
        'Guyana',
        'Paraguay',
        'Peru',
        'Suriname',
        'Uruguay',
        'Venezuela'
        ] and n < 10:
        print(f'{university["ranking"]}. {university["title"]}, \
{university["location"]}')
        n += 1


