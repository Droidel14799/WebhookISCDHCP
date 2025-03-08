from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/Webhook", methods=["POST"])

def hook():
    data = request.json
    print("Received webhook data:", data)
    return jsonify({'message': 'Webhook received successfully'}), 200
 

if __name__=="__main__":
    app.run()