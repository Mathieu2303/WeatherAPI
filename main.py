import requests #testing commit
import json

def get_weather_data(city):
    api_key = '83c8f7fdb9f69377e333be8207a8539c'
    url =  f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    kel_tempature = data['main']['temp']
    far_temp = (1.8(kel_tempature - 273.15)) + 32
    return far_temp


    
    
    
