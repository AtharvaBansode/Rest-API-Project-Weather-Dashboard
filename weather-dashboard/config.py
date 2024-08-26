import os

class Config:
    SECRET_KEY = os.urandom(24)
    WEATHER_API_KEY = '6983cc76b52763cdff4cdef26c79d7eb'  # Replace with your actual API key
    WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'
 
