import urllib
import json
import sys


article_api_prefix = 'https://note.mu/api/v1/notes/'
top_article_base_url = 'https://note.mu/api/v1/top_articles?page='

def read_top_article(page):
    api_url = top_article_base_url + str(page)
    print(api_url)
    readObj = urllib.urlopen(api_url)
    response = readObj.read()
    json_data = json.loads(response)
    return json_data

def article_save(id):
    url = article_api_prefix + id
    print(url)

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
for i in range(1, 10):
    page += 1
    json_data = read_top_article(page)

    data = json_data['data']
    articles = data['articles']
    is_last_page = data['last_page']

    for article in articles:
        id = article['key']
        print(id + ' ' + article['name'])
        article_save(id)

    if is_last_page:
        break