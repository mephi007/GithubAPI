import requests
import re


class reposOperation():
    rep = None
    username = None
    rep_list = []

    def __init__(self,username=None):
        self.username = username
        self.rep = requests.get("https://api.github.com/users/" + username + "/repos").json()
        print(self.rep)

    def list_repo(self, username=None):
        repo = self.rep
        str=[]
        for rep in repo:
            name = rep
            str.append(name["name"])

        return(str)