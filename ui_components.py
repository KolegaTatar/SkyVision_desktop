from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMenu, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


def create_header():
    """ Tworzy nagłówek aplikacji (logo, nawigacja) """
    header_layout = QHBoxLayout()
    header_layout.setContentsMargins(0, 0, 0, 0)  # Usuwamy marginesy na brzegach

    # Dodajemy logo (będzie to tylko tekst na razie)
    logo = QLabel("SkyVision")
    logo.setAlignment(Qt.AlignmentFlag.AlignLeft)
    logo.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffffff; padding: 10px; background-color: #333333; border-radius: 5px;")  # Stylizacja logo
    logo.setFixedHeight(50)  # Ustawiamy wysokość logo na poziomie stopki
    header_layout.addWidget(logo)

    # Tworzymy nawigację
    nav_layout = QHBoxLayout()

    # Tworzymy pełne menu nawigacyjne
    nav_buttons = [
        ("Home", "home_icon.png"),
        ("Prognoza", "forecast_icon.png"),
        ("Miasta", "cities_icon.png"),
        ("Ustawienia", "settings_icon.png"),
        ("Użytkownik", "user_icon.png")
    ]
    
    for label, icon in nav_buttons:
        button = QPushButton(label)
        button.setIcon(QIcon(icon))
        button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-size: 16px;")
        button.setFixedWidth(120)  # Stała szerokość przycisków
        nav_layout.addWidget(button)

    # Dodajemy pełne menu nawigacyjne do headera
    header_layout.addLayout(nav_layout)

    # Tworzymy hamburger menu (będzie widoczny tylko przy węższym ekranie)
    hamburger_button = QPushButton("☰")
    hamburger_button.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 5px; font-size: 24px;")
    hamburger_button.setFixedWidth(50)
    hamburger_button.clicked.connect(lambda: toggle_menu(nav_layout, nav_buttons))

    # Przyciski hamburgera - ukryte na większych ekranach
    header_layout.addWidget(hamburger_button)

    # Tworzymy widget, przypisujemy layout
    header_widget = QWidget()
    header_widget.setLayout(header_layout)  # Zmieniamy to wstawiając poprawnie layout w widget
    return header_widget


def toggle_menu(nav_layout, nav_buttons):
    """ Funkcja przełączająca widoczność hamburger menu """
    for i in range(nav_layout.count()):
        widget = nav_layout.itemAt(i).widget()
        if widget.text() not in [btn[0] for btn in nav_buttons]:
            widget.setVisible(not widget.isVisible())


def create_main_content(app):
    """ Tworzy główną część aplikacji """
    layout = QVBoxLayout()

    # Pole do wpisania miasta
    app.city_input = QLineEdit()
    app.city_input.setPlaceholderText("Wpisz nazwę miasta")
    app.city_input.setStyleSheet("padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc; margin-top: 20px;")
    layout.addWidget(app.city_input)

    # Przycisk do pobrania danych pogodowych
    search_button = QPushButton("Sprawdź pogodę")
    search_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; border-radius: 5px; font-size: 16px; margin-top: 10px;")
    search_button.clicked.connect(app.search_weather)  # Łączenie przycisku z funkcją
    layout.addWidget(search_button)

    # Etykieta do wyświetlania wyników
    app.weather_label = QLabel("Wprowadź miasto i kliknij przycisk")
    app.weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    app.weather_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333333; margin-top: 20px;")
    layout.addWidget(app.weather_label)

    return layout


def create_footer():
    """ Tworzy stopkę aplikacji """
    footer_layout = QHBoxLayout()
    footer_layout.setContentsMargins(0, 0, 0, 0)  # Usuwamy marginesy

    # Tekst stopki
    footer_label = QLabel("Autorzy: Wiktor Tatarynowicz - SkyVision")
    footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    footer_label.setStyleSheet("font-size: 14px; color: #ffffff; background-color: #333333; padding: 10px;")
    footer_layout.addWidget(footer_label)

    footer_widget = QWidget()
    footer_widget.setLayout(footer_layout)
    return footer_widget
