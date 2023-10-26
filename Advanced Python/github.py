import requests
import json


class Github:
    def __init__(self):
        self.apiurl = 'https://api.github.com'
        self.token = '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'

    def find_user(self, username):
        self.username = username
        response = requests.get(self.apiurl + '/users/' + username)
        return response.json()

    def get_Repositories(self,username):
        self.username = username
        response = requests.get(self.apiurl + '/users/' + username+ '/repos')
        return response.json()

    def create_Repository(self,name):
        response = requests.post(self.apiurl + '/user/repos?access_token=' + self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https:/github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()



github = Github()



while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')
    if secim == '1':
        username = input('Username: ')
        result = github.find_user(username)
        print(f'Name: {result["name"]}\nPublic repos: {result["public_repos"]}\nFollowers: {result["followers"]}')
        break
    elif secim == '2':
        username = input('Username: ')
        result = github.get_Repositories(username)
        print(result)
        for repo in result:
            print(repo['name'])
        break
    elif secim == '3':
        name = input('Repository name: ')
        result = github.create_Repository(name)
        print(result)
    elif secim == '4':
        print('Cikis yapildi.')
        break
    else:
        break
