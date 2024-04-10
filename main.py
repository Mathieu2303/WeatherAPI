import requests #testing commit
import json

def get_weather_data(APIkey, city):
    url =  f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  
    else:
        print("failed")
        return None
        

def main():
    api_key = '83c8f7fdb9f69377e333be8207a8539c'
    city_input = input("what city would you like to know the tempature for?")
    get_weather_data(api_key,city_input)
    
    
    
