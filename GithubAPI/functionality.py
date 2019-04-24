import requests as r
user = r.get('https://api.github.com/users/'+'mephi007').json()
print(user)
