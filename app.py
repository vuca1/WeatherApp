from http.client import responses
from idlelib.colorizer import prog_group_name_to_tag

import requests
import tkinter as tk

#obtaines weather info from API
def get_weather(location):
    api_key = "5fd6731a3bc9ae3093279e0d9f973132"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    result = requests.get(url)

    #check if the website is reachable
    if result.status_code == 200:
        data = result.json()
        return data
    else:
        print(f"Error {result.status_code}: Unable to obtain data.")
        return None

#location = input("Location: ")
#weather_data = get_weather(location)

#slices the obtained data into needed information
"""if weather_data:
    city_name = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print(weather_data)
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Wind speed: {wind_speed}")"""

def main():
    #create new window
    window = tk.Tk()
    window.title("Basic Weather App ☁️")
    window.geometry("400x250")

    #input the city
    city_entry = tk.Entry(window, width=35)
    city_entry.pack(pady=15)

    #label for the weather info
    weather_info = tk.Label(window, text="", wraplength=200, justify="center")
    weather_info.pack(pady=10)

    #function to get the weather and update the label for weather info
    def show_weather():
        city = city_entry.get()
        data = get_weather(city)
        if data:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_text = (
                f"City: {city_name}\n"
                f"Temperature: {int(temperature)} °C\n"
                f"Humidity: {humidity} %\n"
                f"Wind speed: {wind_speed} km/h\n"
            )
        else:
            result_text = "Error - Unable to fetch weather data."

        weather_info.config(text=result_text)

    #button to trigger the weather check
    get_weather_button = tk.Button(window, text="Get Weather", command=show_weather)
    get_weather_button.pack(pady=10)

    #bind 'enter' to show the weather
    window.bind("<Return>", lambda event: show_weather())

    #start the GUI
    window.mainloop()



if __name__ == "__main__":
    main()