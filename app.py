from http.client import responses
from idlelib.colorizer import prog_group_name_to_tag

import requests

def get_weather(location):
    api_key = "5fd6731a3bc9ae3093279e0d9f973132"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    result = requests.get(url)

    if result.status_code == 200:
        data = result.json()
        return data
    else:
        print(f"Error {result.status_code}: Unable to obtain data.")
        return None

location = input("Location: ")
weather_data = get_weather(location)


if weather_data:
    print(weather_data)
    print(weather_data["weather"][0]["description"])