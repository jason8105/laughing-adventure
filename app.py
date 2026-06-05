from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("RAPIDAPI_KEY")

@app.route("/instagram")
def instagram():
    username = request.args.get("username")

    url = "https://instagram-scraper-api1.p.rapidapi.com/v2/user_info_by_username"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "instagram-scraper-api1.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params={"username": username}
    )

    return jsonify(response.json())
