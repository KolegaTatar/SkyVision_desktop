# SkyVision - Aplikacja Pogodowa 3D 🌍🌦

**SkyVision** to nowoczesna aplikacja pogodowa oparta na technologii **PyQt6** i **OpenGL**, która oferuje zaawansowaną wizualizację prognoz w formie interaktywnych modeli 3D Ziemi oraz animacji pogody. Aplikacja wykorzystuje dane z API IMGW do wyświetlania informacji o temperaturze, prędkości wiatru i innych parametrach meteorologicznych.

---

## **📋 Spis treści**
1. [Opis aplikacji](#opis-aplikacji)
2. [Wymagania](#wymagania)
3. [Instalacja](#instalacja)
4. [Użycie](#użycie)
5. [Struktura plików](#struktura-plików)
6. [Współpraca](#współpraca)
7. [Licencja](#licencja)

---

## **📌 Opis aplikacji**

**SkyVision** to aplikacja, która umożliwia użytkownikom przeglądanie prognoz pogody w interaktywnej formie 3D. Dzięki zastosowaniu technologii OpenGL i PyQt6 użytkownicy mogą podziwiać trójwymiarowy model Ziemi, na którym wyświetlane są aktualne warunki meteorologiczne. Aplikacja umożliwia:
- Wyświetlanie globalnego modelu Ziemi z dynamicznymi chmurami i pogodą.
- Przewidywanie pogody na podstawie danych pobranych z API IMGW.
- Interaktywne wizualizacje dla różnych miast na świecie.
- Integrację z wykresami temperatury i innych parametrów pogodowych.

---

## **🖥 Wymagania**

Aby uruchomić aplikację, musisz mieć zainstalowane następujące biblioteki:
- **Python 3.x**
- **PyQt6**: do tworzenia aplikacji graficznej.
- **PyOpenGL**: do renderowania grafiki 3D.
- **Matplotlib**: do tworzenia wykresów.
- **Requests**: do pobierania danych z API.

Wymagane wersje bibliotek:
- PyQt6 >= 6.0
- PyOpenGL >= 3.1.5
- Matplotlib >= 3.0
- Requests >= 2.0

---

## **📥 Instalacja**

1. **Pobierz repozytorium**:
   ```bash
   git clone https://github.com/KolegaTatar/SkyVision_desktop
   cd SkyVision
