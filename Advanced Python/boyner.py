import requests
from bs4 import BeautifulSoup

url = "https://www.boyner.com.tr/erkek-ayakkabi-c-2004?OrderOption=SaleQty"

html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')


markelistesi = soup.find("div", {"class":"product-list_productListContainer__Tj820"}).find_all("div","product-item_content__9CfBp")
count = 1

for i in markelistesi:
    marka = i.find("div", {"class":"product-item_brand__LFImW"}).string.strip(' ')
    model = i.find("h3", {"class":"product-item_name__HVuFo"}).string.strip(' ')
    fiyat = i.find("div", {"class":"product-price_checkPrice__NMY9e"}).string.strip(' ')

    print(f"{count}- Urun: {marka} {model.ljust(75)} Fiyat: {fiyat}")
    count +=1


# print(list)