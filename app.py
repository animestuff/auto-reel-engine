from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone, intensity):
    import random

    topic_cap = topic.capitalize()

    # ---------- HOOK BANK ----------
    hook_bank = {
        "aggressive": [
            "Stop lying to yourself.",
            "Wake up.",
            "Enough excuses.",
            "This is your reality check."
        ],
        "calm": [
            "Let’s be honest.",
            "Pause for a second.",
            "Think about this.",
            "Consider this carefully."
        ],
        "dark": [
            "Here’s the uncomfortable truth.",
            "Nobody wants to admit this.",
            "This is why you’re stuck.",
            "Let’s be brutally honest."
        ],
        "luxury": [
            "Top 1% think differently.",
            "High performers understand this.",
            "Winners move differently.",
            "Elite standards create elite results."
        ],
        "viral": [
            "Stop lying to yourself.",
            "This is why you're stuck.",
            "Nobody wants to admit this.",
            "You're avoiding the real problem.",
            "Wake up."
        ]
    }

     # INTENSITY MODIFIER
    if intensity == "viral":
         identity = f"If you care about {topic},"
         tension = "you say you want it, but your actions say otherwise."
         resolution = f"{topic_cap} doesn't reward comfort."
    elif intensity == "high":
         identity = f"If you're serious about {topic},"
         tension = "your habits are exposing you."
         resolution = f"{topic_cap} decides your future."
    elif intensity == "low":
         identity = f"If you're working on {topic},"
         tension = "progress feels slow sometimes."
         resolution = f"Small consistency builds real results."
    else:  # medium/default
        identity = f"If you care about {topic},"
        tension = "you avoid what matters most."
        resolution = f"{topic_cap} shapes your future."

    # ---------- CTA ----------
    if intensity == "viral":
        cta = "Decide who you are."
    else:
        cta = random.choice([
            "Fix it today.",
            "Start acting differently.",
            "Decide who you want to become."
        ])

    # ---------- LOOP LINE ----------
    loop_line = random.choice([
        "Read that again.",
        "Let that sink in.",
        "Think about that.",
        "Now ask yourself why."
    ])

    # ---------- SCRIPT STRUCTURE ----------
    if length == "short":
        full_script = f"{selected_hook} {resolution} {cta}"

    elif length == "medium":
        full_script = f"{selected_hook} {identity} {tension} {resolution} {cta} {loop_line}"

    else:  # long
        full_script = f"{selected_hook} {identity} {tension} {resolution} {cta} {loop_line}"

    hashtags = list(set([
        f"#{topic.lower()}",
        "#mindset",
        "#growth",
        "#discipline"
    ]))

    return {
        "hook": selected_hook,
        "identity": identity,
        "tension": tension,
        "resolution": resolution,
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
    intensity = data.get("intensity", "medium")

    script = generate_script(topic, length, tone, intensity)

    return jsonify(script)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
