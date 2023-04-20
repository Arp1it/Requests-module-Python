import requests

http_proxy = "http://142.132.239.210:8080"
https_proxy = "http://142.132.239.210:8080"

proxies = {
    "http": http_proxy,
    "https": https_proxy
}

url = "https://httpbin.org/get"
r = requests.get(url, data={"a":1, "b":3}, proxies=proxies)
print(r.text)