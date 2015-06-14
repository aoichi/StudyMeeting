import requests

json_file = requests.get('http://connpass.com/api/v1/event/?keyword=python')
print(json_file.text)

