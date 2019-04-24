import requests
import re

class searchOperation():
    username = None
    r = None
    def __init__(self, username=None):
        self.username = username
        self.r = requests.get("https://api.github.com/users/" + username).json()
        print(self.r)

    def ProfilePic(self):
        img_url = self.r["avatar_url"]
        return img_url

    def userName(self):
        name = self.r["name"]
        return name

    def company(self):
        company = self.r["company"]
        return company

    def location(self):
        location = self.r["location"]
        location = location.split(",")
        return location

    newbion= []

    def bio(self):
        bio = self.r["bio"]
        newbio=re.sub("\n|\r", "",bio)
        return newbio

    def repos(self):
        repos = self.r["public_repos"]
        return repos

    def show(self):
        print(self.username)

