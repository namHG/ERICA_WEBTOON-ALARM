import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon'
html = requests.get(url)
#print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup.select_one('#content > div.list_area.daily_all > div:nth-child(1) > div > ul > li:nth-child(1) > a'))
#print(soup.select('div.mon'))
