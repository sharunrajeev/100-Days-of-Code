from dotenv import load_dotenv
from os import environ as env
import requests
from datetime import datetime

load_dotenv()

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutritionix_header = {
    'x-app-id': env['APP_ID'],
    'x-app-key': env['API_KEY'],
    'Content-Type': 'application/json'
}

sheety_header = {
    'Authorization': env['TOKEN']
}

body = {
    'query': input("Which exercise did you do today?\n")
}

res = requests.post(url=nutritionix_endpoint, json=body, headers=nutritionix_header)

exercise_data = res.json()

# Get Date and Time
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')

# Update data into the sheets
sheety_endpoint = 'https://api.sheety.co/096bb1817fdf53024c78e9e2ea415048/myWorkouts/workouts'

for data in exercise_data['exercises']:
    exercise = exercise_data['exercises'][0]['name']
    duration = exercise_data['exercises'][0]['duration_min']
    calories = exercise_data['exercises'][0]['nf_calories']
    body = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
    }
    res = requests.post(url=sheety_endpoint, json=body, headers=sheety_header)
    print(res.text)
