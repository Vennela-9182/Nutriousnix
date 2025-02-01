import requests
import os
from dotenv import load_dotenv
from datetime  import datetime

Authorization=os.getenv("Authorization")
app_key = os.getenv("API_KEY")
app_id = os.getenv("APP_ID")

GENDER="female"
WEIGHT_KG=45
HEIGHT_CM=152
AGE=20
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

activity=result['exercises'][0]['user_input']
calories=result['exercises'][0]['nf_calories']
duration=result['exercises'][0]['duration_min']
today=datetime.now()
date=today.strftime('%d%m%Y')
sheetypara={
  "sheet1": {
    "date": date,
    "duration": duration,
    "activity": activity,
    "calories": calories
  }
}



headers1={
    "Authorization": Authorization
}
sheety_endpoint=f"https://api.sheety.co/811964219f6aa5cd901ac8ac7504a840/myWorkout/sheet1"


response1=requests.post(sheety_endpoint,json=sheetypara,headers=headers1)
print(response1.text)