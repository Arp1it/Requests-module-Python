import requests
from tqdm import tqdm

# url = "https://assets.mixkit.co/active_storage/sfx/2203/2203.wav"
url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"
r = requests.get(url, stream=True)

totalexpectedbytes = int(r.headers["Content-Length"])
print(f"total bytes {totalexpectedbytes}")
bytesReceived = 0
progress_bar = tqdm(total=totalexpectedbytes, unit="iB", unit_scale=True)

# with open("1.wav", 'wb') as f:
with open("winrar.exe", 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        progress_bar.update(128)
        f.write(chunk)
        # print(chunk)
        bytesReceived += 128

progress_bar.close()


# for i in r.iter_content(decode_unicode=True):
#     print(i)
# for i in r.iter_content(decode_unicode=False):
#     print(i)

# for i in r.iter_content(chunk_size=1):
# for i in r.iter_content(chunk_size=2):
#     print(i)

# for i in r.iter_content(chunk_size=2, decode_unicode=True):
#     print(i)
# for i in r.iter_content(chunk_size=2, decode_unicode=False):
#     print(i)