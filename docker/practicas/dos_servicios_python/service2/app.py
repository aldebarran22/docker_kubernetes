import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def call_service1():
    try:
        response = requests.get("http://service1:5000/")  # Llamada al otro servicio
        data = response.json()
        return jsonify({"message": "Hola desde Service2", "response": data})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
