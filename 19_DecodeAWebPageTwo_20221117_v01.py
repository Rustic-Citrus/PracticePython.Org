import requests
from bs4 import BeautifulSoup

source = requests.get('https://en.wikipedia.org/wiki/Sarah_Chapman').text
soup = BeautifulSoup(source, 'lxml')
content = soup.find('div', id='content')
headline = content.h1.text
print(f'{headline}\n')
body_content = content.find('div', id='bodyContent')
subtitle = body_content.div.text
print(f'{subtitle}\n')
mw_content_text = body_content.find('div', id='mw-content-text')
for heading_or_paragraph in mw_content_text.find_all(['h2', 'p']):
    if heading_or_paragraph.text not in ['Contents', 'External links[edit]']:
        print(f'{heading_or_paragraph.text}\n')

reflist = body_content.find('div', class_='reflist')
references = reflist.find('ol', class_='references')
item = 1
for citation in references.find_all('cite', class_='citation web cs1'):
    print(f'{item}. {citation.text}\n')
    item += 1
