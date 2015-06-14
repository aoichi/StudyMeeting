import requests_wrapper


if __name__ == '__main__':
    print('word:', end='')
    keyword = input()
    url = 'http://connpass.com/api/v1/event/?keyword='
    events = requests_wrapper.get_events_from_url(url, keyword)

    f = open('hoge.txt', 'w')
    for item in events:
        output_string = "%05d: %s" % (item['event_id'], item['title'])
        f.write(output_string + '\n')
        print(output_string)
    f.close()
