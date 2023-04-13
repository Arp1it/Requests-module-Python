import requests

r = requests.post('https://httpbin.org/post?a=b', data={'arpit': 'value'})
print(r.text)