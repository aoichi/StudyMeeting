import requests

keyword = input()
url = 'http://connpass.com/api/v1/event/?keyword='

json_file = requests.get(url + keyword)

for item in json_file.json()['events']:
    print(item['event_id'], item['title'])

