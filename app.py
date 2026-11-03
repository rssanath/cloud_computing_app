
from flask import Flask, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def home():
    return "Indian Date and Time API is Running!"

@app.route("/datetime")
def get_datetime():
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    return jsonify({
        "date": now.strftime("%d-%m-%Y"),
        "time": now.strftime("%I:%M:%S %p"),
        "day": now.strftime("%A"),
        "timezone": "IST"
    })

if __name__ == "__main__":
    app.run(debug=True)
