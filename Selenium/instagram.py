from selenium import webdriver
from instagramUser import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.browser.get('https://www.instagram.com')
        time.sleep(1)

        usernameInput = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        time.sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def gelFollowers(self, ):
        i = 1
        self.browser.get(f'https://www.instagram.com/erdm.ys/')
        time.sleep(3)
        self.browser.get(f'https://www.instagram.com/erdm.ys/followers/')
        time.sleep(4)

        dialog = self.browser.find_element(By.CSS_SELECTOR, 'div[role=dialog]')
        followersCount = len(
            dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        print(f"1. count: {followersCount}")

        action = webdriver.ActionChains(self.browser)
        action.send_keys(Keys.TAB).perform()
        time.sleep(1)
        action.send_keys(Keys.TAB).perform()
        time.sleep(1)
        action.send_keys(Keys.TAB).perform()
        time.sleep(1)

        while True:

            action.send_keys(Keys.SPACE).perform()
            time.sleep(1)
            action.send_keys(Keys.SPACE).perform()
            time.sleep(2)
            action.send_keys(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(
                dialog.find_elements(By.CSS_SELECTOR, '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
            print('while true iceren')

            if followersCount != newCount:
                followersCount = newCount
                time.sleep(1)
                print(f'new count = {newCount}')
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements(By.CSS_SELECTOR,
                                         '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
        time.sleep(2)
        print(len(followers))
        followerList = []
        for user in followers:
            name = user.find_element(By.CSS_SELECTOR, '._aacl._aaco._aacw._aacx._aad7._aade').text
            followerList.append(name)
        with open ('followersList.txt', 'w') as file:
            for item in followerList:
                file.write(item + '\n')
        time.sleep(3)

    def followUser(self, username):
        self.browser.get(f'https://www.instagram.com/{username}')
        time.sleep(4)
        followButton = self.browser.find_element(By.CSS_SELECTOR, '._aacl._aaco._aacw._aad6._aade')
        if followButton.text != "Following":
            followButton.click()
            time.sleep(4)
            print(f'{username} takip edildi.')
        else:
            print(f'{username} zaten takip ediliyor')

    def unfollowUser(self, username):
        self.browser.get(f'https://www.instagram.com/{username}')
        time.sleep(2)
        followButton = self.browser.find_element(By.CSS_SELECTOR, '._aacl._aaco._aacw._aad6._aade')
        if followButton.text == "Following":
            followButton.click()
            time.sleep(3)
            unfollow = self.browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]')
            time.sleep(1)
            if unfollow.text == "Unfollow":
                unfollow.click()
                time.sleep(4)
            else:
                unfollow.click()
                time.sleep(2)

            print(f'{username} kullancisini takibi birakti.')
        else:
            print(f'{username} zaten takip edilmiyor')

insta = instagram(username, password)
insta.login()
insta.gelFollowers()
# insta.followUser('')
# insta.unfollowUser('reynmen')
