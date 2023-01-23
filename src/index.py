import requests

res = requests.get("https://beta.decapi.me/twitch/uptime/arikendebu")
print(res.content)