import requests

payload = {'arpit': 'programmer', 'harry': 'big_programmer'}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
print(r.json(), type(r.json()))

# https://httpbin.org/get?arpit=programmer&harry=big_programmer