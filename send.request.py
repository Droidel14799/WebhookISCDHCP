import requests
import json

varprice    = 16.49
varQuantity = 2
varCustomer = "David"
varId       = 44444

#URL to address
url = "http://192.168.178.48:5000/Webhook"

# json format data

dataload = {
"Id": varId,
"Customer": varCustomer,
"Quantity": varQuantity,
"Price": varprice
}


class content:
    def __init__(self, data, url):
        self.data = data
        self.url = url
        headers = {"Content-Type":"application/json"}
        r = requests.post(self.url, headers=headers, data=json.dumps(self.data))
        print(r)


content(dataload, url)
