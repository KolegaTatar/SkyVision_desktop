from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt
from api.imgw_api import get_city_weather
from utils.unit_converter import convert_temperature, convert_pressure, convert_wind_speed
from utils.config import DEFAULT_CITY

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SkyVision - Prognoza Pogody")
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        # Header
        self.create_header(layout)

        # Weather Info Section
        self.create_weather_section(layout)

        # Footer
        self.create_footer(layout)

        # Set the layout
        self.setLayout(layout)

        # Fetch weather for the default city
        self.fetch_weather(DEFAULT_CITY)

    def create_header(self, layout):
        header_layout = QHBoxLayout()
        header_label = QLabel("SkyVision", self)
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        header_layout.addWidget(header_label, alignment=Qt.AlignmentFlag.AlignLeft)

        # You can add buttons for navigation here if needed
        self.settings_button = QPushButton("Ustawienia", self)
        self.settings_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        header_layout.addWidget(self.settings_button, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(header_layout)

    def create_weather_section(self, layout):
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Wpisz miasto...")
        self.city_input.setStyleSheet("padding: 10px; font-size: 16px; margin-top: 20px;")
        layout.addWidget(self.city_input)

        self.search_button = QPushButton("Sprawdź pogodę", self)
        self.search_button.setStyleSheet("background-color: #dfdfdf; color: white; padding: 10px;")
        self.search_button.clicked.connect(self.fetch_weather)
        layout.addWidget(self.search_button)

        self.weather_label = QLabel("Proszę wpisać miasto.", self)
        self.weather_label.setStyleSheet("font-size: 18px; margin-top: 20px;")
        layout.addWidget(self.weather_label)

    def create_footer(self, layout):
        footer_layout = QHBoxLayout()
        footer_label = QLabel("Autorzy: Wiktor Tatarynowicz", self)
        footer_label.setStyleSheet("font-size: 12px; color: white; text-align: center;")
        footer_layout.addWidget(footer_label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(footer_layout)

    def fetch_weather(self, city=None):
        if city is None:  # Jeśli miasto nie zostało przekazane, sprawdzamy pole tekstowe
            city = self.city_input.text().strip()

        # Sprawdzamy, czy miasto jest puste
        if not city:
            self.weather_label.setText("Proszę wpisać miasto.")
            return
        
        # Sprawdzamy, czy miasto zawiera tylko litery (prosta walidacja)
        if not city.isalpha():
            self.weather_label.setText("Miasto powinno zawierać tylko litery.")
            return
        
        # Próba pobrania danych z API
        try:
            weather = get_city_weather(city)

            if not weather:  # Jeśli brak danych z API
                self.weather_label.setText(f"Nie znaleziono miasta: {city}. Sprawdź nazwę.")
                return

            # Pobieramy dane z API (jeśli klucz nie istnieje, zwracamy "Brak danych")
            station = weather.get("stacja", "Brak danych")
            date = weather.get("data_pomiaru", "Brak danych")
            time = weather.get("godzina_pomiaru", "Brak danych")
            temperature = weather.get("temperatura", "Brak danych")
            wind_speed = weather.get("predkosc_wiatru", "Brak danych")
            wind_direction = weather.get("kierunek_wiatru", "Brak danych")
            humidity = weather.get("wilgotnosc_wzgledna", "Brak danych")
            precipitation = weather.get("suma_opadu", "Brak danych")
            pressure = weather.get("cisnienie", "Brak danych")

            # Wyświetlanie danych w GUI
            self.weather_label.setText(f"""
                🌍 Lokalizacja: {station}<br>
                📅 Data: {date}<br>
                ⏰ Godzina: {time}:00<br>
                🌡️ Temperatura: {temperature}°C<br>
                💨 Prędkość wiatru: {wind_speed} km/h<br>
                🧭 Kierunek wiatru: {wind_direction}°<br>
                💧 Wilgotność: {humidity}%<br>
                ☔ Opady: {precipitation} mm<br>
                📈 Ciśnienie: {pressure} hPa<br>
            """)
        except Exception as e:
            self.weather_label.setText(f"Nie udało się połączyć z serwerem. Spróbuj później.")
            print(f"Error fetching data: {e}")
