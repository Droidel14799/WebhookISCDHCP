import requests
import json

varprice    = 16.49
varQuantity = 2
varCustomer = "David"
varId       = 44444

#URL to address
url = "http://127.0.0.1:5000/Webhook"

# header to declare the content-Type
headers = {"Content-Type":"application/json"}

# json format data

dataload = {
"Id": varId,
"Customer": varCustomer,
"Quantity": varQuantity,
"Price": varprice
}


class content:
    def __init__(self, data, url, headers):
        self.data = data
        self.url = url
        self.headers = headers
        r = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        print(r)


content(dataload, url, headers)
