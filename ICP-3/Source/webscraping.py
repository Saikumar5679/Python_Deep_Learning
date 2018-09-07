import requests
from bs4 import BeautifulSoup
import os
a = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(a.text, "html.parser")

print(soup.title.string)

for i in soup.find_all('a'):
    print(i.get("href"))

