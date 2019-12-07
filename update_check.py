import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=sun'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
update = soup.select_one('em.ico_updt')
if(update):
	print("Update!")
else:
	print("Not update.")
