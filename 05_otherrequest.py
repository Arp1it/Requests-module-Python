import requests

r = requests.put('https://httpbin.org/put', data={'key': 'value', "b":3})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
print(r.text)