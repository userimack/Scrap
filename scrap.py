from bs4 import BeautifulSoup

import requests

url = "http://www.video9.in/english"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)


for link in soup.find_all('div',{"class": "updates"}):
    print (link.text)
