import requests
import json
from bs4 import BeautifulSoup
# from requests.api import request
flipkart_link="https://www.flipkart.com/realme-narzo-50a-oxygen-blue-64-gb/p/itm81d679403c2b4?pid=MOBG6MY4UGGFQWYY&lid=LSTMOBG6MY4UGGFQWYYI8WMJQ&marketplace=FLIPKART&q=phone&store=tyy%2F4io&srno=s_1_11&otracker=search&otracker1=search&fm=organic&iid=9155f386-b057-453a-9822-98c6288815ea.MOBG6MY4UGGFQWYY.SEARCH&ppt=None&ppn=None&ssid=noysyho6qo0000001634961721111&qH=f7a42fe7211f98ac"
request=requests.get(flipkart_link)
# print(request.text)
soup=BeautifulSoup(request.text,"html.parser")
# print(soup)

dic={}
Model_Name =soup.find("span",class_="B_NuCI").get_text()
# print(Model_Name)
price=soup.find("div",class_="_30jeq3 _16Jk6d").text
# print(price)
rating=soup.find("div",class_="_3LWZlK").text
# print(rating)

image="https://images2nwck8c0zc.cdn.e2enetworks.net/sangeethaecommerce/product_image/product_details_page/img_20210615_22ae93510410160e15831eef7a6d64cc.jpg"

dic["price"]=price[1:7]
dic["Model_Name"] = Model_Name[0:16]
dic["rating"]=rating
dic["image"]=image
print(dic)

file=open("flipkart.json","w")
json.dump(dic,file,indent=4)

