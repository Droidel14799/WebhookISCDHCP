import requests
import json

#URL to address

url = "http://127.0.0.1:5000/Webhook"

# header to declare the content-Type

headers = {"Content-Type":"application/json"}

# json format data

data = {
"Id": 12345,
"Customer": "David",
"Quantity": 1,
"Price": 19.99
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r)