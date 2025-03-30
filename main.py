import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QSurfaceFormat
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
import requests

# API URL dla pogody
API_URL = "https://danepubliczne.imgw.pl/api/data/synop"

# Funkcja pobierająca dane pogodowe
def get_weather_data(city):
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            if entry["stacja"].lower() == city.lower():
                return {
                    "temperature": entry["temperatura"],
                    "wind_speed": entry["predkosc_wiatru"],
                    "pressure": entry["cisnienie"]
                }
    return None

# Klasa do obsługi OpenGL w aplikacji
class WeatherAppWindow(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.weather_data = None

    def initializeGL(self):
        """Inicjalizuje OpenGL tylko raz."""
        print("Inicjalizowanie OpenGL...")
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Kolor tła
        glEnable(GL_DEPTH_TEST)  # Włączanie testu głębokości
        
        # Ustawienie macierzy projekcji w initializeGL
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()  # Zerowanie macierzy
        gluPerspective(45.0, self.width() / self.height(), 0.1, 100.0)  # Perspektywa

        glMatrixMode(GL_MODELVIEW)  # Ustawienie trybu model-view

    def resizeGL(self, w, h):
        """Zmiana rozmiaru okna i ustawianie perspektywy."""
        print(f"Zmiana rozmiaru okna: {w}x{h}")
        
        glMatrixMode(GL_PROJECTION)  # Ustawiamy tryb macierzy projekcji
        glLoadIdentity()  # Zerowanie macierzy
        
        if h == 0:
            h = 1  # Unikamy dzielenia przez zero
        gluPerspective(45.0, float(w) / float(h), 0.1, 100.0)  # Perspektywa
        glMatrixMode(GL_MODELVIEW)  # Przechodzimy do trybu model-view

    def paintGL(self):
        """Rysowanie sceny w OpenGL."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Czyszczenie bufora
        glLoadIdentity()  # Zerowanie macierzy widoku
        glTranslatef(0.0, 0.0, -6.0)  # Przesunięcie kamery
        
        glBegin(GL_TRIANGLES)  # Rysowanie trójkątów
        glColor3f(1.0, 0.0, 0.0)  # Ustawienie koloru na czerwony
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()

    def search_weather(self, city):
        """Funkcja wywoływana po naciśnięciu przycisku - pobiera dane o pogodzie."""
        self.weather_data = get_weather_data(city)

        if self.weather_data:
            weather_info = f"Temperatura: {self.weather_data['temperature']}°C\n"
            weather_info += f"Prędkość wiatru: {self.weather_data['wind_speed']} km/h\n"
            weather_info += f"Ciśnienie: {self.weather_data['pressure']} hPa"
        else:
            weather_info = "Nie znaleziono danych dla tego miasta."

        # Zwracamy dane pogodowe do głównego okna, by wyświetlić je w QLabel
        return weather_info


# Główna funkcja uruchamiająca aplikację
def main():
    app = QApplication(sys.argv)

    # Tworzymy format powierzchni dla OpenGL
    format = QSurfaceFormat()
    format.setVersion(4, 1)  # Ustawiamy wersję OpenGL
    QSurfaceFormat.setDefaultFormat(format)  # Ustawiamy domyślny format dla aplikacji

    # Tworzymy główne okno aplikacji
    window = QWidget()
    window.setWindowTitle("Weather App")

    # Tworzymy instancję klasy WeatherAppWindow (okno z OpenGL)
    weather_window = WeatherAppWindow()

    # Tworzymy widget do wprowadzenia nazwy miasta
    city_input = QLineEdit()
    city_input.setPlaceholderText("Wpisz nazwę miasta")

    # Tworzymy przycisk do wyszukiwania pogody
    search_button = QPushButton("Sprawdź pogodę")

    # Tworzymy etykietę do wyświetlania wyników
    weather_label = QLabel("Wyniki pogodowe")

    # Funkcja uruchamiająca wyszukiwanie pogody po kliknięciu przycisku
    def on_search_button_clicked():
        city = city_input.text()
        weather_info = weather_window.search_weather(city)
        weather_label.setText(weather_info)

    # Łączymy funkcję wywołania przycisku z metodą on_search_button_clicked
    search_button.clicked.connect(on_search_button_clicked)

    # Layout do ustawienia widgetów w oknie
    layout = QVBoxLayout()
    layout.addWidget(city_input)
    layout.addWidget(search_button)
    layout.addWidget(weather_label)
    layout.addWidget(weather_window)

    window.setLayout(layout)

    # Pokazujemy okno aplikacji
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
