import requests

json_file = requests.get('http://connpass.com/api/v1/event/?keyword=python')

for item in json_file.json()['events']:
    print(item['event_id'], item['title'])

