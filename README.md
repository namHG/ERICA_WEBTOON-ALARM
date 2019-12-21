# ERICA_WEBTOON-ALARM
2019018795 소프트웨어학부 남현기

crawling.py : 웹툰의 제목을 알려준다.

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=fri'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('ul.img_list')
for i in title_list:
    print(i.select_one('dt > a').text.strip())

url을 바꾸면 요일별 웹툰의 제목을 가져올 수 있다.
