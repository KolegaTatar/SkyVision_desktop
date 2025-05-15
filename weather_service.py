import requests
from datetime import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather?q="
KEY = "24b50d974e7a48aecd763a1605f548df"

def get_weather_data(city):
    """Pobiera dane pogodowe dla podanego miasta z OpenWeatherMap."""
    try:
        # Budowanie URL z miastem i kluczem API
        url = f"{API_URL}{city}&appid={KEY}&units=metric&lang=pl"  # units=metric, lang=pl dla temperatury w °C i odpowiedzi po polsku
        response = requests.get(url)
        response.raise_for_status()

        # Przetwarzanie danych JSON
        data = response.json()

        # Sprawdzamy, czy odpowiedź zawiera dane pogodowe
        if response.status_code == 200 and data.get("cod") == 200:
            # Pobieramy dane
            city_name = data["name"]
            country = data["sys"]["country"]
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]
            weather_description = data["weather"][0]["description"]
            weather_icon = data["weather"][0]["icon"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            visibility = data["visibility"]
            wind_speed = data["wind"]["speed"]
            wind_deg = data["wind"]["deg"]
            clouds = data["clouds"]["all"]
            sunrise_timestamp = data["sys"]["sunrise"]
            sunset_timestamp = data["sys"]["sunset"]
            timezone = data["timezone"]

            # Konwertowanie czasu wschodu i zachodu słońca do formatu godziny
            sunrise_time = datetime.utcfromtimestamp(sunrise_timestamp + timezone).strftime('%H:%M:%S')
            sunset_time = datetime.utcfromtimestamp(sunset_timestamp + timezone).strftime('%H:%M:%S')

            return {
                "weather_html": f"""
                    🌍 Lokalizacja: {city_name}, {country}<br>
                    🌐 Koordynaty: ({lat}, {lon})<br>
                    ☀️ Opis pogody: {weather_description} <img src="http://openweathermap.org/img/wn/{weather_icon}.png"><br>
                    🌡️ Temperatura: {temperature}°C (odczuwalna: {feels_like}°C)<br>
                    🌡️ Temperatura minimalna: {temp_min}°C, Temperatura maksymalna: {temp_max}°C<br>
                    💧 Wilgotność: {humidity}%<br>
                    📈 Ciśnienie: {pressure} hPa<br>
                    👁️ Widoczność: {visibility / 1000} km<br>
                    💨 Prędkość wiatru: {wind_speed} km/h<br>
                    🧭 Kierunek wiatru: {wind_deg}°<br>
                    ☁️ Chmury: {clouds}%<br>
                    🌅 Wschód słońca: {sunrise_time}<br>
                    🌇 Zachód słońca: {sunset_time}<br>
                """
            }
        else:
            return {
                "error": f"Nie znaleziono danych dla miasta: {city}. Sprawdź nazwę miasta."
            }

    except requests.exceptions.RequestException:
        return {"error": "⚠️ Błąd połączenia z serwerem OpenWeatherMap. Sprawdź internet."}
    except ValueError:
        return {"error": "⚠️ Błąd przetwarzania danych. API mogło zwrócić błędną odpowiedź."}


