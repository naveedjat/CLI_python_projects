import requests

response = requests.get("Your Api Key")
data = response.json()
quote = data[0]['q']
author = data[0]['a']

print(f"{quote} — {author}")
