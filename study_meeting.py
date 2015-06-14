import requests

html_file = requests.get('http://google.com')
print(html_file.text)
