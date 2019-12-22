import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=sun'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
update = soup.select_one('em.ico_updt')
if(update):
    update = update.find_parent('ul', class_= 'img_list')
    title = update.select_one('li:nth-child(1) > dl > dt > a').text.strip()
    print(title + " is updated!\n")
else:
    print("Not updated.\n")
