import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon'
html = requests.get(url)
print(html.text)
