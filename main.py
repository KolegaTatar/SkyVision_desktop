import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_components import WeatherUI
from weather_service import get_weather_data

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SkyVision - Prognoza Pogody")
        self.setGeometry(100, 100, 800, 600)

        self.weather_ui = WeatherUI(self.search_weather)
        self.setCentralWidget(self.weather_ui)

    def search_weather(self, city):
        return get_weather_data(city)

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
