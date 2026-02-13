from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone):

    tone = tone.lower()

    hooks = {
        "aggressive": [
            "Listen carefully.",
            "Stop lying to yourself.",
            "This is your wake-up call.",
            "Enough excuses."
        ],
        "calm": [
            "Think about this.",
            "Pause for a second.",
            "Let’s reflect.",
            "Consider this carefully."
        ],
        "dark": [
            "Here’s the uncomfortable truth.",
            "Nobody wants to admit this.",
            "This is why you’re stuck.",
            "Let’s be brutally honest."
        ],
        "luxury": [
            "High performers understand this.",
            "Top 1% think differently.",
            "Elite mindset only.",
            "Winners operate like this."
        ]
    }

    default_hooks = ["Let’s talk about this."]
    selected_hook = random.choice(hooks.get(tone, default_hooks))

    topic = topic.capitalize()

    if length == "short":
        body = f"{topic} shapes your future. Your habits decide your results."
        cta = "Act now."

    elif length == "medium":
        body = f"You say you want success in {topic}. But your habits say otherwise. Discipline creates results."
        cta = "Fix your focus."

    elif length == "long":
        body = f"Most people blame {topic} for their failures. But growth begins when you stop avoiding discomfort."
        cta = "Master your habits."

    else:
        body = f"{topic} determines your direction. Choose wisely."
        cta = "Start today."

    full_script = f"{selected_hook} {body} {cta}"

    hashtag_map = {
        "discipline": ["#discipline", "#selfcontrol", "#growth", "#mindset"],
        "success": ["#success", "#winning", "#growth", "#mindset"],
        "focus": ["#focus", "#clarity", "#discipline", "#productivity"]
    }

    hashtags = hashtag_map.get(topic.lower(), [f"#{topic.lower()}", "#mindset", "#growth"])

    return {
        "hook": selected_hook,
        "body": body,
        "cta": cta,
        "full_script": full_script,
        "hashtags": hashtags
    }



@app.route("/")
def home():
    return "Auto Reel Engine is running 🚀"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    topic = data.get("topic", "success")
    length = data.get("length", "short")
    tone = data.get("tone", "default")

    script = generate_script(topic, length, tone)
    return jsonify(script)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
