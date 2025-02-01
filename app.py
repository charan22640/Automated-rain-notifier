import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio Credentials from .env
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TO_PHONE = os.getenv("TO_PHONE")
FROM_PHONE = os.getenv("FROM_PHONE")

# OpenWeather API Credentials
API_KEY = os.getenv("WEATHER_API_KEY")
MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")

# Weather API Parameters
parameters = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4
}

# Fetch weather data
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()

# Check if it rains
will_rain = any(hourly["weather"][0]["id"] < 700 for hourly in data["list"])

if will_rain:
    print("Bring an umbrella!")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to=TO_PHONE,
        from_=FROM_PHONE,
        body="Hey, get an umbrella!"
    )
    print("Message sent:", message.sid)
