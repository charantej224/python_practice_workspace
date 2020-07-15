import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"
auth = requests.auth.HTTPBasicAuth(username='charantej', password='Password*01')
params = {'project': 'sample1', 'owner': 'charantej', 'output': 'null', 'format': 'default-plus-annjson'}
with open('ann.json', 'r') as f:
    annotations = f.read()
files = {
    'ann': ('text.ann.json', annotations),
    'plain': ('text.txt', open('./text.txt'))
}

response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print('process complete to upload annotations and file.')
