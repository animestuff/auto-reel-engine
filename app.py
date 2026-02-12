from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


def generate_script(topic):
    hooks = [
        f"Stop blaming {topic}.",
        f"You’re not bad at {topic}. You’re undisciplined.",
        f"Nobody talks about this in {topic}."
    ]

    tension = [
        f"You say you want results in {topic}, but your habits say otherwise.",
        f"You complain about {topic}, yet repeat the same mistakes.",
        f"You want success in {topic}, but avoid discomfort."
    ]

    truth = [
        f"{topic.capitalize()} rewards discipline, not emotion.",
        f"{topic.capitalize()} exposes who you really are.",
        f"{topic.capitalize()} doesn’t care about your excuses."
    ]

    command = [
        "Fix your habits.",
        "Choose growth over comfort.",
        "Decide who you want to become."
    ]

    return f"{random.choice(hooks)} {random.choice(tension)} {random.choice(truth)} {random.choice(command)}"

@app.route("/")
def home():
    return "Auto Reel Engine is running 🚀"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    topic = data.get("topic", "success")

    script = generate_script(topic)

    return jsonify({
        "topic": topic,
        "script": script
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
