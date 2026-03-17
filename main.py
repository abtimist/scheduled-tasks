import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


client = Client(account_sid, auth_token)

weather_params = {
    "lat":25.2973,
    "lon":91.5827,
    "appid":api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()

weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        messaging_service_sid = os.environ.get("MSG_SERVICE_ID"),
        body = 'Bring an Umbrella ☔',
        to = os.environ.get("PHONE_NO")
    )
    print(message.status)






