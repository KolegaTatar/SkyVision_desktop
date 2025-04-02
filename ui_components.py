from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class WeatherUI(QWidget):
    def __init__(self, search_weather_callback):
        super().__init__()

        self.search_weather_callback = search_weather_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        self.header = QLabel("🌤️ SkyVision - Pogoda na dziś", self)
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(self.header)

        # Input for city name
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Wpisz nazwę miasta...")
        self.city_input.setStyleSheet("padding: 5px; font-size: 16px;")
        layout.addWidget(self.city_input)

        # Search button
        self.search_button = QPushButton("🔍 Sprawdź pogodę", self)
        self.search_button.clicked.connect(self.search_weather)
        self.search_button.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.search_button)

        # Weather label to show weather info
        self.weather_label = QLabel("Tu pojawi się pogoda...", self)
        self.weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weather_label.setStyleSheet("font-size: 18px; margin-top: 10px;")
        layout.addWidget(self.weather_label)

        self.setLayout(layout)

    def search_weather(self):
        city = self.city_input.text().strip()
        if city:
            weather_data = self.search_weather_callback(city)
            if "error" in weather_data:
                self.weather_label.setText(weather_data["error"])
            else:
                self.weather_label.setText(weather_data["weather_html"])
        else:
            self.weather_label.setText("✍️ Wpisz nazwę miasta!")
