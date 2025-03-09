from flask import Flask, request, jsonify
from waitress import serve
import re

config_path="ISCDHCP.conf"
listenIP="0.0.0.0"
port="5000"

app = Flask(__name__)
def check(para,regstring, config_path=config_path):
    with open(config_path, "r") as file:
        content = file.read()
    
    return bool(re.search(fr"{regstring} {para};", content))

def check_MAC(mac):
     return check(mac, "hardware ethernet")
    
def check_ip(ip):
     return check(ip, "fixed-address")

def check_name(name):
     return check(name, "option host-name")

# Beispiel-Aufruf
def check_host(mac,ip,name):
    if check_MAC(mac):
        print(f"Ein Datensatz mit folgender MAC: {mac} existiert bereits.")
        return False
    elif check_ip(ip):
         print(f"Ein Datensatz mit folgender IP: {ip} existiert bereits.")
         return False
    elif check_name(name):
         print(f"Ein Datensatz mit folgendem Namen: {name} existiert bereits.")
         return False
    else:
        print("Host nicht gefunden, kann hinzugefügt werden.")
        return True

def add_dhcp_host(MAC, IP, Hostname):
        print("Adding Host")
        new_entry = f"""
host {Hostname} {{
    hardware ethernet {MAC};
    fixed-address {IP};
    option host-name "{Hostname}";
}}"""
        with open(config_path, "a") as file:
            file.write(new_entry)

@app.route("/Webhook", methods=["POST"])

def hook():
    data = request.json
    IP = data['IP']
    MAC= data['MAC']
    Hostname= data['Hostname']
    if not check_host(MAC,IP,Hostname):
         print("Abort...")
    else:
        add_dhcp_host(MAC, IP, Hostname)
    return jsonify({'message': 'Webhook received successfully'}), 200
 
if __name__=="__main__":

     serve(app, host=listenIP, port=port)
    