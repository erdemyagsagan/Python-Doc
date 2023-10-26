from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
url = "https://maltepe.edu.tr"
driver.get(url)
searchInput = driver.find_element(By.XPATH,'//*[@id="txtSearchWebSiteQuery"]')
time.sleep(2)
searchInput.send_keys("bilgisayar")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

siteSource = soup.find("div", {"class":"page-news-list search-result-list"}).find_all("div",{"class":"pnl-item-title"})
# print(siteSource)
for isimler in siteSource:
    print(isimler.text.strip())







time.sleep(2)
driver.close()