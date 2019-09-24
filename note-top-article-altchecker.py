import urllib
import json
import sys
import re
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
article_api_prefix = 'https://note.mu/api/v1/notes/'
top_article_base_url = 'https://note.mu/api/v1/top_articles?page='

def read_top_article(page):
    api_url = top_article_base_url + str(page)
    print(api_url)
    readObj = urllib.urlopen(api_url)
    response = readObj.read()
    json_data = json.loads(response)
    return json_data


for page in range(1, 21):
    json_data = read_top_article(page)

    data = json_data['data']
    articles = data['articles']
    is_last_page = data['last_page']

    for article in articles:
        id = article['key']
        name = article['name']
        body = article['free_body']
        publish_at = article['publish_at']
        if body:
            print("(%s)<%s>"%(publish_at,id))
            print(name)
            altlist = re.findall(r'alt="[^"]*"', body)
            for alt in altlist:
                print(alt)


    if is_last_page:
        print('last page')
        break