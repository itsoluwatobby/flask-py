import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
  print("\n*** Get Current Weather Conditions ***\n")

  city = input("\nPlease enter a city name: ")

  WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

  weather_data = requests.get(WEATHER_URL).json()
  # pprint(weather_data)
  print(f"\nCurrent Weather for {weather_data['name']}")
  print(f"\nTemperature is: {weather_data['main']['temp']}")
  print(f"\nFeels like: {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}.")

if __name__ == '__main__':
  get_current_weather()