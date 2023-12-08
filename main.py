import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ["OWM_API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
from_number = os.environ["FROM_NUMBER"]
to_number = os.environ["TO_NUMBER"]

weather_params = {
    "lat": os.environ["LAT"],
    "lon": os.environ["LON"],
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

weather_conditions = [data["list"][index]["weather"][0]["id"] for index in range(4)]
for code in weather_conditions:
    if code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=from_number,
            body="It's going to rain today. Remember to bring an umbrella.",
            to=to_number
        )
        print(message.status)
        break
