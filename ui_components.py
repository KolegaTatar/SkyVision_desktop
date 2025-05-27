# ui_components.py
from PyQt6.QtCore import Qt, QFile, QIODevice, QTextStream
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton,
                             QHBoxLayout, QLabel, QFrame, QGridLayout, QSpacerItem,
                             QSizePolicy)


class WeatherUI(QWidget):
    def __init__(self, search_weather_callback):
        super().__init__()
        self.search_weather_callback = search_weather_callback
        self.icons = {}  # Inicjalizacja słownika ikon
        self.load_icons()  # Najpierw ładujemy ikony
        self.load_styles()
        self.init_ui()

    def load_icons(self):
        self.icons = {
            'search': self.create_icon("🔍"),
            'sunrise': self.create_icon("🌅"),
            'sunset': self.create_icon("🌇"),
            'humidity': self.create_icon("💧"),
            'pressure': self.create_icon("📊"),
            'wind': self.create_icon("💨"),
            'thermo': self.create_icon("🌡️"),
            'air': self.create_icon("🍃")
        }

    def create_icon(self, emoji):
        label = QLabel(emoji)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label

    def load_styles(self):
        file = QFile("styles.qss")
        if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Search Section
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Wpisz nazwę miejscowości...")
        self.city_input.setMinimumHeight(45)

        self.search_button = QPushButton()
        self.search_button.setFixedSize(45, 45)
        self.search_button.setObjectName("searchButton")
        self.search_button.clicked.connect(self.search_weather)

        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.search_button)
        main_layout.addLayout(search_layout)

        # Current Weather Section
        current_weather_frame = QFrame()
        current_weather_frame.setObjectName("currentWeatherFrame")
        current_weather_layout = QVBoxLayout()
        current_weather_layout.setSpacing(10)
        current_weather_frame.setLayout(current_weather_layout)

        # City and time
        self.city_label = QLabel("Warszawa")
        self.city_label.setObjectName("cityLabel")
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_label = QLabel("Pogoda teraz - dzisiaj godz. 20:04")
        self.time_label.setObjectName("timeLabel")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        current_weather_layout.addWidget(self.city_label)
        current_weather_layout.addWidget(self.time_label)

        # Sunrise/sunset
        sun_layout = QHBoxLayout()
        sun_layout.setSpacing(20)

        sunrise_container = QHBoxLayout()
        sunrise_container.setObjectName("sunriseContainer")
        sunrise_container.addWidget(self.icons['sunrise'])
        self.sunrise_label = QLabel("05:08")
        sunrise_container.addWidget(self.sunrise_label)

        sunset_container = QHBoxLayout()
        self.sunset_label = QLabel("19:58")
        sunset_container.addWidget(self.sunset_label)
        sunset_container.addWidget(self.icons['sunset'])

        sun_layout.addLayout(sunrise_container)
        sun_layout.addStretch()
        sun_layout.addLayout(sunset_container)
        current_weather_layout.addLayout(sun_layout)

        # Weather condition
        self.weather_condition = QLabel("Przelotne opady")
        self.weather_condition.setObjectName("weatherCondition")
        self.weather_condition.setAlignment(Qt.AlignmentFlag.AlignCenter)
        current_weather_layout.addWidget(self.weather_condition)

        # Temperature
        temp_layout = QHBoxLayout()
        temp_layout.addWidget(self.icons['thermo'])
        self.temperature_label = QLabel("ODCZUWALNA 16°C")
        self.temperature_label.setObjectName("temperatureLabel")
        temp_layout.addWidget(self.temperature_label)
        temp_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        current_weather_layout.addLayout(temp_layout)

        # Additional info grid
        info_grid = QGridLayout()
        info_grid.setHorizontalSpacing(20)
        info_grid.setVerticalSpacing(10)

        # Humidity
        info_grid.addWidget(self.icons['humidity'], 0, 0)
        self.humidity_label = QLabel("WILGOTNOŚĆ")
        self.humidity_label.setObjectName("infoLabel")
        info_grid.addWidget(self.humidity_label, 0, 1)
        self.humidity_value = QLabel("26%")
        self.humidity_value.setObjectName("infoValue")
        info_grid.addWidget(self.humidity_value, 0, 2)

        # Pressure
        info_grid.addWidget(self.icons['pressure'], 1, 0)
        self.pressure_label = QLabel("CIŚNIENIE")
        self.pressure_label.setObjectName("infoLabel")
        info_grid.addWidget(self.pressure_label, 1, 1)
        self.pressure_value = QLabel("1019 hPa")
        self.pressure_value.setObjectName("infoValue")
        info_grid.addWidget(self.pressure_value, 1, 2)

        # Wind
        info_grid.addWidget(self.icons['wind'], 2, 0)
        self.wind_label = QLabel("WIATR")
        self.wind_label.setObjectName("infoLabel")
        info_grid.addWidget(self.wind_label, 2, 1)
        self.wind_value = QLabel("17 km/h")
        self.wind_value.setObjectName("infoValue")
        info_grid.addWidget(self.wind_value, 2, 2)

        current_weather_layout.addLayout(info_grid)
        main_layout.addWidget(current_weather_frame)

        # Bottom buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)

        self.hourly_btn = QPushButton("POGODA GODZINA PO GODZINIE")
        self.hourly_btn.setObjectName("hourlyButton")

        self.daily_btn = QPushButton("POGODA NA 45 DNI")
        self.daily_btn.setObjectName("dailyButton")

        self.holiday_btn = QPushButton("POGODA NA MAJÓWKĘ")
        self.holiday_btn.setObjectName("holidayButton")

        buttons_layout.addWidget(self.hourly_btn)
        buttons_layout.addWidget(self.daily_btn)
        buttons_layout.addWidget(self.holiday_btn)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def search_weather(self):
        city = self.city_input.text().strip()
        if city:
            weather_data = self.search_weather_callback(city)
            if "error" in weather_data:
                self.city_label.setText("❗")
                self.weather_condition.setText(weather_data["error"])
            else:
                self.update_weather_ui(weather_data)
        else:
            self.weather_condition.setText("✍️ Podaj miasto.")

    def update_weather_ui(self, data):
        self.city_label.setText(f"{data.get('city', '-')}, {data.get('country', '-')}")
        current_time = data.get('current_time', 'brak danych')
        self.time_label.setText(f"Pogoda teraz - dzisiaj godz. {current_time}")
        self.sunrise_label.setText(data.get('sunrise', '-'))
        self.sunset_label.setText(data.get('sunset', '-'))
        self.weather_condition.setText(data.get("description", "Brak opisu").capitalize())
        feels_like = data.get('feels_like', '-')
        self.temperature_label.setText(f"ODCZUWALNA {feels_like}°C" if feels_like != '-' else "ODCZUWALNA -")
        humidity = data.get('humidity', '-')
        self.humidity_value.setText(f"{humidity}%" if humidity != '-' else "-")
        pressure = data.get('pressure', '-')
        self.pressure_value.setText(f"{pressure} hPa" if pressure != '-' else "-")
        wind_speed = data.get('wind_speed', '-')
        self.wind_value.setText(f"{wind_speed} km/h" if wind_speed != '-' else "-")


