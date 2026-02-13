import requests
from datetime import datetime

API_KEY = "bdffc12ea046c5f705689e5cdccd42"   #API wont work as the actual API KEY is kept hidden.. This is a dummy API
base_url = "https://api.openweathermap.org/data/2.5"

def get_coordinates(city):
    url= f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city,"appid": API_KEY}
    response = requests.get(url, params=params).json()

    lat = response["coord"]["lat"]
    lon = response["coord"]["lon"]
    return lat, lon

def get_7days_forecast(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "current,minutely,hourly,alerts",
        "appid": API_KEY,
        "units": "metric"
    }
    return requests.get(url, params=params).json()

city = input("Enter city name: ")
lat, lon = get_coordinates(city)
forecast_data = get_7days_forecast(lat, lon)

for day in forecast_data["list"][:7]:
    date = datetime.fromtimestamp(day["dt"]).strftime("%H:%M %d-%m")
    temp_min = day["main"]["temp_min"]
    temp_max = day["main"]["temp_max"]
    condition = day["weather"][0]["description"]

    print(f"{date} : {temp_max}°C - {condition}")

