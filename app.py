from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("RAPIDAPI_KEY")

@app.route("/media")
def media():
    shortcode = request.args.get("shortcode")

    response = requests.get(
        "https://instagram-scraper-ai1.p.rapidapi.com/media_id/from_shortcode/",
        headers={
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": "instagram-scraper-ai1.p.rapidapi.com",
            "Content-Type": "application/json"
        },
        params={"shortcode": shortcode}
    )

    return jsonify(response.json())

@app.route("/")
def home():
    return "API is running!"
