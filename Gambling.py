import requests
import json
from bs4 import BeautifulSoup

url="https://affyo.com/networks/gamblingpro/"
req_data=requests.get(url)
soup=BeautifulSoup(req_data.text,"html.parser")
# print(soup)

data1=soup.find_all("li",class_="ne-ta").text
print(data1)
# data2=soup.find("div",class_="cl").a["href"]
# print(data2)

# <div class="cl"></div>