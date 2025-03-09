from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)


def add_dhcp_host(MAC, IP, Hostname):
        print("Adding Host")
        config_path="ISCDHCP.conf"
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
    add_dhcp_host(MAC, IP, Hostname)
    return jsonify({'message': 'Webhook received successfully'}), 200
 
if __name__=="__main__":

     serve(app, host="0.0.0.0", port=5000)
    