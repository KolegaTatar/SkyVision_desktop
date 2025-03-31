# 🌤️ **SkyVision  - Aplikacja Pogodowa**  

SkyVision  to nowoczesna aplikacja pogodowa napisana w **Pythonie** z wykorzystaniem **PyQt6**. Umożliwia użytkownikom sprawdzanie aktualnej pogody dla wybranego miasta, korzystając z danych z **IMGW**.  

---

## 📌 **Funkcje**  

✅ **Prognoza Pogody** – temperatura, prędkość wiatru, ciśnienie atmosferyczne  
✅ **Minimalistyczny i nowoczesny interfejs** – przejrzysty i intuicyjny design  
✅ **Motywy kolorystyczne** – jasny i ciemny tryb  
✅ **Obsługa różnych jednostek** – °C/°F, km/h/m/s, hPa/mmHg  
✅ **Łatwa instalacja** – działa na **Windows, Linux i macOS**  
✅ **Dane z IMGW** – aktualne informacje pogodowe  

---

## 🛠️ **Technologie**  

🔹 **Python 3** – Główny język programowania  
🔹 **PyQt6** – Nowoczesny framework GUI  
🔹 **requests** – Pobieranie danych pogodowych  
🔹 **QSS (Qt Style Sheets)** – Stylizacja aplikacji  

---

## 🚀 **Instalacja i Uruchomienie**  

### **1️⃣ Sklonuj repozytorium**  
```bash
git clone https://github.com/KolegaTatar/SkyVision_desktop
cd SkyVision 
```

### **2️⃣ Zainstaluj wymagane biblioteki**  
Upewnij się, że masz **Python 3** zainstalowany, a następnie:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Uruchom aplikację**  
```bash
python main.py
```

---

## 🎨 **Motywy Interfejsu**  

WeatherPro obsługuje dwa motywy:  
🌞 **Jasny Motyw** (`styles_light.qss`)  
🌙 **Ciemny Motyw** (`styles_dark.qss`)  

Motywy można zmieniać w ustawieniach aplikacji.  

---

## 🌍 **Źródło Danych**  

Aplikacja pobiera dane pogodowe z:  
🔹 **[IMGW](https://danepubliczne.imgw.pl/api/data/synop)** – Polska baza meteorologiczna  

---

## 🛠️ **Struktura Projektu**  

```
📂 WeatherPro/
├── 📜 main.py          # Główny plik aplikacji
├── 📂 api/             # Obsługa API IMGW
│   ├── imgw_api.py     # Pobieranie danych pogodowych
├── 📂 ui/              # Interfejs użytkownika
│   ├── main_window.py  # Główne okno aplikacji
│   ├── styles.qss      # Stylizacja aplikacji
├── 📂 utils/           # Dodatkowe funkcje
│   ├── config.py       # Ustawienia aplikacji
│   ├── unit_converter.py # Konwersja jednostek
├── 📜 requirements.txt  # Lista wymaganych bibliotek
└── 📜 README.md        # Dokumentacja projektu
```

---

## 👨‍💻 **Autorzy**  

WeatherPro zostało stworzone przez:  
- **Wiktor Tatarynowicz** – Główny programista  

### 📝 **Współpraca**  

WeatherPro to projekt **open-source**. Jeśli masz pomysły na nowe funkcje lub znalazłeś błąd – zgłoś problem lub zaproponuj zmianę!  

📢 **Dziękujemy za korzystanie z WeatherPro!** 🚀