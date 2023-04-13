import requests

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())