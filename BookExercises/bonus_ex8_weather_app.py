#Allows for interaction with APIs
import requests

API_KEY = "4ecf3434e36ca39603a0c809a5ed09ba" # Replace with your actual API key
city = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Temperature in {city}: {data['main']['temp']} °C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("City not found!")