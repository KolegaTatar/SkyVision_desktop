def convert_temperature(value, unit="Celsius"):
    """Konwertuje temperaturę między Celsjuszem a Fahrenheitem."""
    if unit == "Fahrenheit":
        return round((float(value) * 9/5) + 32, 2)
    return round(float(value), 2)

def convert_pressure(value, unit="hPa"):
    """Konwertuje ciśnienie między hPa a mmHg."""
    if unit == "mmHg":
        return round(float(value) * 0.75006, 2)
    return round(float(value), 2)

def convert_wind_speed(value, unit="km/h"):
    """Konwertuje prędkość wiatru między km/h a m/s."""
    if unit == "m/s":
        return round(float(value) / 3.6, 2)
    return round(float(value), 2)
