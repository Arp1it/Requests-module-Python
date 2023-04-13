import requests
from io import BytesIO

# url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"
# r = requests.get(url)

# fp = open("winrar.exe", "wb")
# fp.write(r.content)
# fp.close()


url = "https://assets.mixkit.co/active_storage/sfx/2203/2203.wav"
r = requests.get(url)

# fp = open("1.mp3", "wb")
fp = open("1.wav", "wb")
fp.write(r.content)
fp.close()