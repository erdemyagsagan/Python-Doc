from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://github.com'
driver.get(url)

time.sleep(2)
driver.maximize_window()
time.sleep(2)
print(driver.title)
time.sleep(2)
driver.save_screenshot("homepage.png")

time.sleep(2)
driver.close()


