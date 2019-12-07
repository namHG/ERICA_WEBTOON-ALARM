import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
day = soup.select('div.col col_selected')
#title = day.select('div.thumb')
print(day)
#for i in title:
#    print(i.select_one('a > em').text.strip())
