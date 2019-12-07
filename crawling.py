import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=sun'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('ul.img_list')
for i in title_list:
    print(i.select_one('dt > a').text.strip())
