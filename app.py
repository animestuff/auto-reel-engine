from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone):
    import random

    tone = tone.lower()

    hooks = {
        "aggressive": [
            "Stop lying to yourself.",
            "Wake up.",
            "No more excuses.",
            "Listen carefully."
        ],
        "calm": [
            "Let’s be honest.",
            "Think about this.",
            "Pause for a second.",
            "Consider this."
        ],
        "dark": [
            "Here’s the uncomfortable truth.",
            "Nobody talks about this.",
            "This is why you're stuck.",
            "Let’s be brutally honest."
        ],
        "luxury": [
            "High performers understand this.",
            "Successful people know this.",
            "Top 1% think differently.",
            "Winners move differently."
        ]
    }

    selected_hook = random.choice(hooks.get(tone, ["Listen carefully."]))

    if length == "short":
        truth = f"{topic.capitalize()} shapes your future."
        tension = "Your habits decide your results."
        cta = "Act now."

    elif length == "medium":
        truth = f"You say you want success in {topic}."
        tension = "But your habits say otherwise."
        cta = "Fix your focus."

    else:  # long
        truth = f"Most people blame {topic} for their failures."
        tension = "But growth begins when you stop avoiding discomfort."
        cta = "Master your habits."

    full_script = f"{selected_hook} {truth} {tension} {cta}"

    return {
        "hook": selected_hook,
        "truth": truth,
        "tension": tension,
        "cta": cta,
        "full_script": full_script,
        "hashtags": [f"#{topic}", "#mindset", "#discipline"]
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
