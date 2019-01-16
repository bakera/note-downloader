import urllib
import json
import sys

args = sys.argv
if len(args) <= 1:
    print('Usage: ' + args[0] + ' {note_id}')
    print('example: python ' + args[0] + ' mefab063665cc')
    sys.exit()

article_api_prefix = 'https://note.mu/api/v1/notes/'
magazine_api_prefix = 'https://note.mu/api/v1/layout/magazine/'
magazine_api_suffix = '/section?page='
id = args[1]
magazine_base_url = magazine_api_prefix + id + magazine_api_suffix

def read_magazine(page):
    readObj = urllib.urlopen(magazine_base_url + str(page))
    response = readObj.read()
    json_data = json.loads(response)
    return json_data

def article_save(id):
    url = article_api_prefix + id

    readObj = urllib.urlopen(url)
    response = readObj.read()
    json_data = json.loads(response)

    body = json_data['data']['body']
    filename = id + '.html'

    with open(filename, 'w') as fp:
        fp.write(body.encode('UTF-8'))

    print('saved:' + filename)

page = 0
article_count = 0
while True:
    page += 1
    json_data = read_magazine(page)

    section = json_data['data']['section']
    articles = section['contents']
    total_count = section['total_count']
    is_last_page = section['is_last_page']

    for article in articles:
        print(article['key'] + ' ' + article['name'])
        article_save(article['key'])

    article_count += int(len(articles))
    if is_last_page or article_count >= total_count:
        break

