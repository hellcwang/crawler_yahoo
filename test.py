import requests
import re
from bs4 import BeautifulSoup

r = requests.get("https://tw.news.yahoo.com/%E4%BD%99%E8%8B%91%E7%B6%BA%E5%BF%8D%E7%97%9B%E6%85%B6%E7%94%9F-%E5%A5%B3%E5%85%92%E6%90%B6%E8%A8%B1%E9%A1%987%E5%AD%97%E5%93%AD%E7%88%86-064003172.html")
s = BeautifulSoup(r.text, 'html.parser')
t = s.find('div', {"class":"caas-img-container"})
print(t)
i = t.find('img')
print(i)
print(i['data-src'])

for i in t:
    #print(str(i))
    if(re.search("class", str(i)) != None):
        print(i['src'])
        break
print()

t = s.find("img", {"class":"caas-img.has-preview.caas-loaded"})
print(t)

