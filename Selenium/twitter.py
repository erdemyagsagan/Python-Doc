from selenium import webdriver
from twitterUser import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password


    def signIn(self):
        self.browser.get('https://twitter.com/i/flow/login')
        time.sleep(3)

        usernameInput = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        time.sleep(1)
        usernameInput.send_keys(username)
        time.sleep(1)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(1)
        passwordInput = self.browser.find_element(By.NAME, 'password')
        passwordInput.send_keys(password)
        time.sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(1)
    def search(self,hashtag):
        time.sleep(4)
        searchInput = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        time.sleep(1)
        searchInput.send_keys(hashtag)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        results = []
        # tweetList = self.browser.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
        # for tweet in tweetList:
        #     print("*****************")
        #     print(tweet.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:
            if loopCounter > 3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(1)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter += 1

            list = self.browser.find_elements(By.XPATH,"//div[@data-testid='tweet']/div[2]/div[2]")
            time.sleep(1.5)
            print("count: " + str(len(list)))

            for i in list:
                results.append(i.text)
        tweetList = self.browser.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
        time.sleep(2)
        for tweet in tweetList:
            print("*****************")
            print(tweet.text)


twit = Twitter(username,password)
twit.signIn()
twit.search('python')
