import requests
from cachetools import TTLCache

API_KEY = "02181a2eac3ea0b70f1f1d859dfc1b9f"  

def create_weather_session():
    """
    Create a session for making API requests with retries in case of connection errors.
    """
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount('http://', adapter)
    return session

def get_weather_data(session, location):
    """
    Get weather data from the OpenWeatherMap API for the specified location.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": API_KEY, "q": location, "units": "metric"}
    response = session.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data, host_name):
    """
    Display the weather information for the specified location.
    """
    if weather_data is not None:
        main_data = weather_data["main"]
        wind_data = weather_data["wind"]
        weather_description = weather_data["weather"][0]["description"]

        print("\nCurrent Weather Information:")
        print(f"Location: {weather_data['name']}")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Wind Speed: {wind_data['speed']} m/s")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Forecast delivered by: {host_name}")
    else:
        print("Error: Unable to retrieve weather data. Please check the city/zip code and try again.")

def weather_forecast_app():
    session = create_weather_session()
    cache = TTLCache(maxsize=100, ttl=300)  # Cache data for 5 minutes

    print("Welcome to the Weather Forecast Application!")
    location = "Mathura,IN"  
    host_name = "Vidhan"  

    if location in cache:
        weather_data = cache[location]
    else:
        weather_data = get_weather_data(session, location)
        cache[location] = weather_data

    display_weather(weather_data, host_name)

if __name__ == "__main__":
    weather_forecast_app()