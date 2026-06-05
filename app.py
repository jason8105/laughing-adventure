from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("RAPIDAPI_KEY")

@app.route("/")
def home():
    return "Instagram Username API is running!"

@app.route("/instagram")
def instagram():
    username = request.args.get("username")

    if not username:
        return jsonify({"error": "Missing username parameter"}), 400

    response = requests.get(
        "https://instagram-scraper-ai1.p.rapidapi.com/user/info_v2/",
        headers={
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": "instagram-scraper-ai1.p.rapidapi.com",
            "Content-Type": "application/json"
        },
        params={"username": username}
    )

    try:
        return jsonify(response.json())
    except Exception:
        return jsonify({
            "status_code": response.status_code,
            "raw_response": response.text
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
