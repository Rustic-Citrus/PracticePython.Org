import requests
from bs4 import BeautifulSoup
import datetime

x = requests.get('https://www.reuters.com/world/americas/')

soup = BeautifulSoup(x.content, 'html5lib')

media_story_cards = soup.findAll('div', attrs={"data-testid": "MediaStoryCard"})
headings = soup.findAll('a', attrs={"data-testid": "Heading"})

headlines = []

for n in range(len(headings)-1):
    headlines.append(headings[n].text)

print(f"REUTERS HEADLINES FOR THE AMERICAS @ {datetime.datetime.today()}")

for n in range(10):
    print(f"STORY #{n+1}: {headlines[n]}")
