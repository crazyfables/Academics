import requests

url = "http://127.0.0.1:8080"
# url = "https://www.blizzard.com/"
req = requests.get(url)

print(req.text)