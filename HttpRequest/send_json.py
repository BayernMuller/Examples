import requests, json
url = 'http://localhost:8080/'
headers = {'Content-Type' : 'application/json; charset=utf-8'}
data = {'x' : 123 }
res = requests.post(url, headers = headers, data=json.dumps(data))
print(res.text)