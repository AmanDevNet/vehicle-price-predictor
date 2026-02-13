
import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    "Year": 2015,
    "Present_Price": 5.59,
    "Kms_Driven": 27000,
    "Owner": 0,
    "Fuel_Type": "Petrol",
    "Seller_Type": "Dealer",
    "Transmission": "Manual"
}

try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Success!")
        print("Prediction:", response.json())
    else:
        print("Failed:", response.status_code)
        print("Response:", response.text)
except Exception as e:
    print("Error:", e)
