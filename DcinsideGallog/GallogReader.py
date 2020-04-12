import requests
from bs4 import BeautifulSoup

user_id = input('input User ID : ')
url = 'https://gallog.dcinside.com/' + user_id + '/comment'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
pages = html.find_all(class_='bottom_paging_box')[0].find_all('a')

last_page = str(pages[-1].get('href'))
last_page = int(last_page[last_page.find('=') + 1 : len(last_page)])

for page in range(1, last_page + 1):
	comment_url = url + '/?p=' + str(page)
	response = requests.get(comment_url)
	html = BeautifulSoup(response.text, 'html.parser')
	comments = html.find(class_='cont_listbox').find_all('li')
	for comment in comments:
		tags = comment.find_all('a')
		if (tags[1].text is ''):
			print('(DC_CON)')
			continue
		print(tags[1].text)
