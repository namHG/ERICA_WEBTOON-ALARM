import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=sun'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
update = soup.select_one('em.ico_updt')
if(update):
    update = update.find_parent('div', class_= 'list_area daily_img')
    title = update.select_one('li:nth-child(2) > dl > dt > a').text.strip()
    update2 = update.select_one('li:nth-child(2) > div > a > em')
    if(update2):
        print(title + " is updated!\n")
    else:
        print("Not updatede!\n")
else:
    print("Not updated.\n")
