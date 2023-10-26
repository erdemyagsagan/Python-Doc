from selenium import webdriver
from githubUserInfo import username,password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def sigIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(0)

        usernamee = self.browser.find_element(By.XPATH,'//*[@id="login_field"]')
        passwordd = self.browser.find_element(By.XPATH,'//*[@id="password"]')

        usernamee.send_keys(self.username)
        passwordd.send_keys(self.password)
        time.sleep(0)
        login = self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[13]')
        login.click()

    def followersAppend(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed')
        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR, '.Link--secondary').text)
    def getFollowers(self):
        self.browser.get("https://github.com/erdem?&tab=followers")
        self.followersAppend()
        while True:
            links = self.browser.find_element(By.CLASS_NAME,'pagination').find_elements(By.TAG_NAME,'a')
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    self.followersAppend()
                else:
                    break
            else:
                for link in links:
                    if link.text =="Next":
                        link.click()
                        time.sleep(2)
                        self.followersAppend()
                    else:
                        continue

github = Github(username,password)
github.sigIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)

