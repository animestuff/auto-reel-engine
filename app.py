from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


def generate_script(topic):
    hooks = [
        f"You think {topic} is the problem.",
        f"Nobody tells you the truth about {topic}.",
        f"If you ignore {topic}, you stay average.",
    ]

    bodies = [
        f"The way you approach {topic} decides your future.",
        f"Most people misunderstand {topic}, and that’s why they fail.",
        f"Mastering {topic} separates winners from watchers.",
    ]

    endings = [
        "Change your mindset. Change your life.",
        "Start today. Or stay stuck.",
        "The choice is yours.",
    ]

    return f"{random.choice(hooks)} {random.choice(bodies)} {random.choice(endings)}"

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
