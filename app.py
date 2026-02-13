from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone):
    import random

    topic_cap = topic.capitalize()

    # Scroll stopper hooks
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
            "Elite mindset only."
        ]
    }

    selected_hook = random.choice(hook_bank.get(tone, ["Listen carefully."]))

    # Identity trigger
    identity_triggers = [
        f"If you care about {topic},",
        f"If you truly want success in {topic},",
        f"If you're serious about improving {topic},",
        f"If you're tired of failing in {topic},"
    ]

    identity = random.choice(identity_triggers)

    # Emotional tension
    tension_bank = [
        "your habits are exposing you.",
        "your discipline is inconsistent.",
        "your comfort zone is winning.",
        "your actions don’t match your goals."
    ]

    tension = random.choice(tension_bank)

    # Resolution
    resolution_bank = [
        "Growth begins when discomfort becomes normal.",
        "Discipline decides your future.",
        "Consistency beats motivation every time.",
        "Your identity shapes your destiny."
    ]

    resolution = random.choice(resolution_bank)

    # CTA + loop style ending
    cta_bank = [
        "Fix it today.",
        "Start acting differently.",
        "Decide who you want to become.",
        "Or stay the same."
    ]

    cta = random.choice(cta_bank)

    if length == "short":
        full_script = f"{selected_hook} {resolution} {cta}"
    elif length == "medium":
        full_script = f"{selected_hook} {identity} {tension} {resolution} {cta}"
    else:
        full_script = f"{selected_hook} {identity} {tension} {resolution} {cta} Read that again."

    return {
        "hook": selected_hook,
        "identity": identity,
        "tension": tension,
        "resolution": resolution,
        "cta": cta,
        "full_script": full_script,
        "hashtags": [f"#{topic.lower()}", "#mindset", "#discipline", "#growth"]
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
