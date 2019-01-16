import urllib
import json
import sys

args = sys.argv
if len(args) <= 1:
    print('Usage: ' + args[0] + ' {note_id}')
    print('example: python ' + args[0] + ' nf50862365649')
    sys.exit()

api_prefix = 'https://note.mu/api/v1/notes/'
id = args[1]
url = api_prefix + id

readObj = urllib.urlopen(url)
response = readObj.read()
json_data = json.loads(response)

body = json_data['data']['body']
filename = id + '.html'

with open(filename, 'w') as fp:
    fp.write(body.encode('UTF-8'))

print('saved:' + filename)