from flask import Flask, request, jsonify
from waitress import serve


app = Flask(__name__)

@app.route("/Webhook", methods=["POST"])

def hook():
    data = request.json
    print(f"Die ID ist vom Kunden {data['Customer']} ist ", data['Id'])
    return jsonify({'message': 'Webhook received successfully'}), 200
 

if __name__=="__main__":

    serve(app, host="0.0.0.0", port=5000)