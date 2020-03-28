import sys
import requests
import json
url = 'http://ecos.bok.or.kr/api/StatisticItemList/sample/json/kr/1/9/064Y001/0089000/'
response = requests.get(url)
if not response:
	print('Failed to request')
	sys.exit(0)

string = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
print(string)