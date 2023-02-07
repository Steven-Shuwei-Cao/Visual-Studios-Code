import requests

def get_weather(location):
    api_key = "9f7d94bff1ac90714ba5fe4a73ca1e39"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"The weather in {location} is {weather} and the temperature is {round(temp-272.15, 2)}°C.")
    else:
        print("Error: Could not retrieve weather data.")

get_weather("Bridgewater, New Jersey")
