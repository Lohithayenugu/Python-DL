import requests as rq
from bs4 import BeautifulSoup

response=rq.get("https://en.wikipedia.org/wiki/Deep_learning")
cont=BeautifulSoup(response.content,"html.parser")
print("Title")
print("-----------------------------------------------------------------------------------------------------------------------\n")
print(cont.title.string)
atags=cont.find_all("a")
print("\nAnchor tag references")
print("-----------------------------------------------------------------------------------------------------------------------\n")
for i in atags:
    print(i.get("href"))
