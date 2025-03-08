import requests
import json

class content:
    def __init__(self, data, url, headers):
        self.data = data
        self.url = url
        self.headers = headers
        r = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        print(r)


#URL to address

url = "http://127.0.0.1:5000/Webhook"

# header to declare the content-Type

headers = {"Content-Type":"application/json"}

# json format data

dataload = {
"Id": 12345,
"Customer": "David",
"Quantity": 1,
"Price": 19.99
}

content(dataload, url, headers)
