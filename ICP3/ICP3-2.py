import requests as rq
from bs4 import BeautifulSoup

response=rq.get("https://en.wikipedia.org/wiki/Deep_learning")
cont=BeautifulSoup(response.content,"html.parser")
print("Title")
print("-----------------------------------------------------------------------------------------------------------------------\n")
print(cont.title.string)
print(cont.text)
f=open("input.txt", "w+")
f.write(cont.text)
f.close()
