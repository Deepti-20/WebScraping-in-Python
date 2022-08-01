import requests
import json
from bs4 import BeautifulSoup

clothes_link = "https://www.boohoo.com/basic-stretch-denim-skirt-/FZZ05238.html?color=340"
req=requests.get(clothes_link)
# print(req.text)
soup=BeautifulSoup(req.text,"html.parser")
# print(soup)
dic={}
colour=soup.find("span",class_="selected-value").text
# print(colour)
size=soup.find("ul",class_="swatches size clearfix").text.split()
# print(size)
price=soup.find("span",class_="price-standard").text
print(price)
dic["colour"]=colour[1:9]
dic["size"]=size
dic["price"]=price[2:7]
# print(dic)

file=open("hooboo_clothes.json","w")
json.dump(dic,file,indent=4)
# <img class="swatchanchor-img ls-is-cached lazyloaded" src="//media.boohoo.com/i/boohoo/fzz05238_light%20blue_xl_s.jpg?$product_image_swatch$&amp;fmt=webp" data-url="//media.boohoo.com/i/boohoo/fzz05238_light%20blue_xl_s.jpg?$product_image_swatch$" alt="light blue" data-src="//media.boohoo.com/i/boohoo/fzz05238_light%20blue_xl_s.jpg?$product_image_swatch$&amp;fmt=webp">

