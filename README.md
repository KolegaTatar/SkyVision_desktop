# 🌤️ SkyVision - Aplikacja Pogodowa

SkyVision to elegancka i intuicyjna aplikacja do sprawdzania prognozy pogody w czasie rzeczywistym. Korzysta z OpenWeatherMap API, aby dostarczać aktualne informacje o warunkach atmosferycznych na całym świecie.

## 🚀 Funkcjonalności
- 🌍 Pobieranie danych pogodowych na podstawie nazwy miasta
- 🌡️ Wyświetlanie temperatury, wilgotności, ciśnienia i innych parametrów
- ☀️ Wizualizacja ikon pogodowych i czasu wschodu/zachodu słońca
- 💨 Informacje o wietrze, widoczności i zachmurzeniu
- 🎨 Nowoczesny interfejs użytkownika oparty na PyQt6

## 🖥️ Zrzuty ekranu
*(Tutaj możesz dodać zrzuty ekranu aplikacji)*

## 🔧 Wymagania
- Python 3.8+
- PyQt6
- requests

## 📦 Instalacja

1. **Sklonuj repozytorium**:
    ```sh
    git clone https://github.com/twoj-profil/skyvision.git
    cd skyvision
    ```

2. **Zainstaluj wymagane zależności**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Uruchom aplikację**:
    ```sh
    python main.py
    ```

## 🛠️ Struktura projektu
```
skyvision/
│── main.py                 # Główna logika aplikacji
│── weather_service.py      # Pobieranie danych pogodowych z API
│── ui_components.py        # Interfejs użytkownika
│── styles2.qss             # Plik stylów aplikacji
│── README.md               # Dokumentacja projektu
```

## 🌍 API i Klucz
Aplikacja wykorzystuje OpenWeatherMap API. Aby ją uruchomić, zarejestruj się na [OpenWeatherMap](https://openweathermap.org/) i uzyskaj klucz API.

Zmień zmienną `KEY` w pliku `weather_service.py`:
```python
KEY = "TWOJ_KLUCZ_API"
```

## 🤝 Współpraca
Chcesz dodać nowe funkcje lub poprawić istniejące? Zapraszamy do współtworzenia! Forkuj repozytorium i twórz Pull Requesty.

## 📜 Licencja
Projekt jest dostępny na licencji MIT.

---
🎯 **SkyVision – Twój osobisty asystent pogodowy!**

