from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello from Flask Backend!"})

@app.route("/api/health")
def health_check():
    return jsonify({"status": "healthy", "service": "groups-up-backend"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))