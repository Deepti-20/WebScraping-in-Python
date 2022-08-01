import json
import requests
from bs4 import BeautifulSoup

phone_link="https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree"
req_phone = requests.get(phone_link)
data=BeautifulSoup(req_phone.text,"html.parser")
# print(data)

mobile_brand=data.find("svg",class_="IIvmWM").text
print(mobile_brand)

