import requests
import json



MAC         = "00:1A:2B:3C:4D:FF"
IP          = "192.168.178.130"
Hostname    = "TestHostTest"
#URL to address
url = "http://127.0.0.1:5000/Webhook"

# json format data

dataload = {
"MAC": MAC,
"IP": IP,
"Hostname": Hostname,
}


class content:
    def __init__(self, data, url):
        self.data = data
        self.url = url
        headers = {"Content-Type":"application/json"}
        r = requests.post(self.url, headers=headers, data=json.dumps(self.data))
        print(r)


content(dataload, url)
