import requests
r = requests.get('https://api.github.com/users/harshsingh262')
print(r)
print(r.content)