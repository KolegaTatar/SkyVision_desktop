import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import WeatherApp

def load_stylesheet(file_path):
    """ Wczytuje arkusz stylów QSS """
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] Nie znaleziono pliku stylów: {file_path}")
        return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Wczytaj arkusz stylów
    stylesheet = load_stylesheet("ui/styles.qss")
    if stylesheet:
        app.setStyleSheet(stylesheet)

    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
