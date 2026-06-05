from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("RAPIDAPI_KEY")

@app.route("/")
def home():
    return "Instagram API is running!"

@app.route("/instagram")
def instagram():
    username = request.args.get("username")

    if not username:
        return jsonify({
            "error": "Please provide a username"
        }), 400

    response = requests.get(
        "https://instagram-scraper-api1.p.rapidapi.com/v2/user_info_by_username",
        headers={
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": "instagram-scraper-api1.p.rapidapi.com"
        },
        params={"username": username}
    )

    return jsonify({
        "status_code": response.status_code,
        "response": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
