import requests

url = "http://localhost:8000/predict"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
result = response.json()
prob = result['probability']
print(f"The probability that this client will get a subscription is: {prob:.3f}")

# Options: 0.334, 0.534, 0.734, 0.934
options = [0.334, 0.534, 0.734, 0.934]
closest = min(options, key=lambda x: abs(x - prob))
print(f"Closest option: {closest}")
