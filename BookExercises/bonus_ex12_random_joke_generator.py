import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url, timeout=5)
if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']}\n - {joke['punchline']}")
else:
    print("Couldn't fetch a joke!")
