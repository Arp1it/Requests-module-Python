import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://images.unsplash.com/photo-1575936123452-b67c3203c357?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8&w=1000&q=80")
i = Image.open(BytesIO(r.content))
fp = open("img.jpg", "wb")
i.save(fp)
fp.close()