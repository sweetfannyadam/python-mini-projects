import requests
from datetime import datetime
import os
import json

# NUTRITIONIX
APP_ID = None  # use os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = None  # use os.environ.get("NUTRITIONIX_API_KEY")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
nutritionix_body = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
nutritionix_get_response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_body)
data_get = nutritionix_get_response.json()
print(data_get)

DATETIME = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")
EXERCISE = data_get["exercises"][0]["name"]
DURATION = data_get["exercises"][0]["duration_min"]
CALORIES = data_get["exercises"][0]["nf_calories"]

# SHEETY
sheety_endpoint = None  # use os.environ.get("SHEETY_ENDPOINT")
sheety_headers = None  # use json.loads(os.environ.get("SHEETY_TOKEN"))

add_row_body = {
    "workout": {
        "date": DATETIME,
        "time": TIME,
        "exercise": EXERCISE.title(),
        "duration": DURATION,
        "calories": CALORIES
    }
}

add_row_response = requests.post(url=sheety_endpoint, json=add_row_body, headers=sheety_headers)
print(add_row_response.text)
