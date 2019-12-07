import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=mon'
html = requests.get(url)
#print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup.select_one('#content > div.list_area.daily_img > ul > li:nth-child(1) > dl > dt > a'))
#print(soup.select('div.mon'))
