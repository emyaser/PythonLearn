import requests

start_url='https://bbs.hupu.com/bxj'
repos = requests.get(start_url).text
print(repos)