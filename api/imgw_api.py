import requests

API_URL = "https://danepubliczne.imgw.pl/api/data/synop"

def get_weather_data():
    """Pobiera dane pogodowe z API IMGW."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Błąd pobierania danych: {e}")
        return None

def get_city_weather(city):
    """Zwraca dane pogodowe dla wybranego miasta."""
    data = get_weather_data()
    if data:
        for entry in data:
            if entry["stacja"].lower() == city.lower():
                return entry
    return None
