import os
from bs4 import BeautifulSoup

for files in os.listdir("htmls"):
    # print(files)
    with open(f"htmls/{files}") as f:
        htmlcontent = f.read()
        soup = BeautifulSoup(htmlcontent, "html.parser")
        # print(soup)
        # print(soup.title)
        for link in soup.findAll("a"):
            # print(link)
            print(link.get("href"))