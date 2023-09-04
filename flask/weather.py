from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city='Ibadan'):
    WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(WEATHER_URL).json()

    if weather_data['cod'] == 200:
        return weather_data
    return {"cod": weather_data['cod'], 'message': weather_data['message']}


if __name__ == '__main__':
    print('\n***Get Current Weather Conditions***\n')
    city = input('Please enter a city name: ')

    # checks for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'Lagos'

    weather_data = get_current_weather(city)
    pprint(weather_data)
