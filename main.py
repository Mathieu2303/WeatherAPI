import requests #testing commit
import json

def get_weather_data(city):
    api_key = '83c8f7fdb9f69377e333be8207a8539c'
    url =  f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    tempature = data['main']['temp']
    return tempature


    
    
    
