import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=mon'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
update = soup.select_one('em.ico_updt')
if(update):
    update = update.find_parent('div', class_= 'list_area daily_img')
    title = update.select_one('li:nth-child(7) > dl > dt > a').text.strip()
    print(title + " is updated!\n")
else:
    print("Not updated.\n")
