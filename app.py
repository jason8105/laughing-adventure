from flask import Flask, request, jsonify
from worker import process_job
import uuid

app = Flask(__name__)

jobs = {}

@app.route("/")
def home():
    return "Bot running"

@app.route("/bulk_submit", methods=["POST"])
def bulk_submit():
    data = request.json
    links = data.get("links", [])

    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "processing", "result": []}

    process_job(job_id, links, jobs)

    return jsonify({"job_id": job_id})

@app.route("/result/<job_id>")
def result(job_id):
    return jsonify(jobs.get(job_id, {"error": "not found"}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
