import requests


def get_events_from_url(url, keyword):
    json_file = requests.get(url + keyword)
    return json_file.json()['events']