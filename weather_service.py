import requests

# API URL dla pogody
API_URL = "https://danepubliczne.imgw.pl/api/data/synop"

def get_weather_data(city):
    """ Pobiera dane pogodowe dla podanego miasta """
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            if entry["stacja"].lower() == city.lower():
                return {
                    "temperature": entry["temperatura"],
                    "wind_speed": entry["predkosc_wiatru"],
                    "pressure": entry["cisnienie"]
                }
    return None
