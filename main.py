from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from ui_components import create_header, create_footer, create_main_content


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SkyVision")
        self.setGeometry(100, 100, 800, 600)
        
        self.initUI()

    def initUI(self):
        """Inicjalizacja interfejsu użytkownika."""
        main_layout = QVBoxLayout()

        # Tworzymy nagłówek i dodajemy go do layoutu
        header_widget = create_header()
        main_layout.addWidget(header_widget)

        # Tworzymy główną część aplikacji
        main_content = create_main_content(self)
        main_layout.addLayout(main_content)

        # Tworzymy stopkę i dodajemy ją do layoutu
        footer_widget = create_footer()
        main_layout.addWidget(footer_widget)

        # Główny widget, który będzie zawierał wszystko
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def search_weather(self):
        """Funkcja do pobrania pogody po kliknięciu przycisku."""
        city = self.city_input.text()
        if city:
            # Możesz tutaj dodać kod do pobierania danych pogodowych.
            self.weather_label.setText(f"Pogoda dla {city} jest teraz dostępna!")
        else:
            self.weather_label.setText("Proszę wpisać nazwę miasta.")
    

def main():
    app = QApplication([])
    window = WeatherApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
