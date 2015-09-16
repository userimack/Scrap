
from bs4 import BeautifulSoup

 #for using urllib module
import urllib   # for using urlib module
response = urllib.urlopen("http://video9.in/english/")
html = response.read()
soup = BeautifulSoup(html,"html.parser")


'''#for using urllib2 , Request module
import urllib2  # for using urllib2 module
req = urllib2.Request("http://video9.in/english/")

response = urllib2.urlopen(req)
html = response.read()

soup = BeautifulSoup(html,"html.parser")
'''

''' #for using requests module

import requests

url = "http://video9.in/english/"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)
'''

for link in soup.find_all('div',{"class": "updates"}):
    print (link.text)





