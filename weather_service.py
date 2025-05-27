import requests
from datetime import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather?q="
KEY = "24b50d974e7a48aecd763a1605f548df"

def get_weather_data(city):
    """Pobiera dane pogodowe dla podanego miasta z OpenWeatherMap."""
    try:
        url = f"{API_URL}{city}&appid={KEY}&units=metric&lang=pl"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if response.status_code == 200 and data.get("cod") == 200:
            timezone = data["timezone"]

            # Konwersja bieżącego czasu (UTC + przesunięcie strefy)
            current_time = datetime.utcfromtimestamp(data["dt"] + timezone).strftime('%H:%M:%S')

            sunrise_time = datetime.utcfromtimestamp(data["sys"]["sunrise"] + timezone).strftime('%H:%M:%S')
            sunset_time = datetime.utcfromtimestamp(data["sys"]["sunset"] + timezone).strftime('%H:%M:%S')

            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "temp_min": data["main"]["temp_min"],
                "temp_max": data["main"]["temp_max"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "visibility": data.get("visibility", 0),
                "wind_speed": data["wind"]["speed"],
                "wind_deg": data["wind"]["deg"],
                "clouds": data["clouds"]["all"],
                "sunrise": sunrise_time,
                "sunset": sunset_time,
                "current_time": current_time
            }
        else:
            return {
                "error": f"Nie znaleziono danych dla miasta: {city}. Sprawdź nazwę miasta."
            }

    except requests.exceptions.RequestException:
        return {"error": "⚠️ Błąd połączenia z serwerem OpenWeatherMap. Sprawdź internet."}
    except ValueError:
        return {"error": "⚠️ Błąd przetwarzania danych. API mogło zwrócić błędną odpowiedź."}
