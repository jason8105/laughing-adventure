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

    data = response.json()

    try:
        user = data["data"]["user"]

        return jsonify({
            "username": user.get("username"),
            "full_name": user.get("full_name"),
            "user_id": user.get("pk"),
            "followers": user.get("follower_count"),
            "following": user.get("following_count"),
            "verified": user.get("is_verified"),
            "private": user.get("is_private"),
            "biography": user.get("biography"),
            "profile_pic": user.get("profile_pic_url"),
            "external_url": user.get("external_url")
        })

    except Exception:
        return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
