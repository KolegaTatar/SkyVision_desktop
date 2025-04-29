# weather_service.py
import requests
from datetime import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather?q="
KEY = "24b50d974e7a48aecd763a1605f548df"

def get_weather_data(city):
    try:
        url = f"{API_URL}{city}&appid={KEY}&units=metric&lang=pl"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            return {"error": f"Nie znaleziono miasta: {city}"}

        current_time = datetime.now().strftime('%H:%M')
        sunrise_time = datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime('%H:%M')
        sunset_time = datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime('%H:%M')

        return {
            "current_time": current_time,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "sunrise": sunrise_time,
            "sunset": sunset_time
        }
    except Exception as e:
        return {"error": "⚠️ Błąd pobierania danych."}