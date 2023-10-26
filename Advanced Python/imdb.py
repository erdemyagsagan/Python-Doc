import requests
from bs4 import BeautifulSoup

url = "https://www.sinemalar.com/filmler/en-iyi-filmler"

html = requests.get(url).content
soup = BeautifulSoup(html,'html.parser')

filmlistesi = soup.find("div",{"class":"movies"}).findAll("div",{"class":"details"})
print(filmlistesi)

# for film in filmlistesi:
#     name = film.find("div", {"class": "name"}).string.strip()
#     year = film.find("div", {"class": "item"}).text.strip()
#
#     # rating = film.find("div", {"class": "right-top-info"})
#     # print(rating)
#     print(name.ljust(45),year)
#

# print(list)