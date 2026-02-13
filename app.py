from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone, intensity):
    import random

    topic_cap = topic.capitalize()

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
        ],
        "viral": [
            "Stop lying to yourself.",
            "This is why you're stuck.",
            "Nobody wants to admit this.",
            "You're avoiding the real problem.",
            "Wake up."
       ],

    }

    selected_hook = random.choice(hook_bank.get(tone, ["Listen carefully."]))

    identity_triggers = [
        f"If you care about {topic},",
        f"If you're serious about improving {topic},",
        f"If you truly want success in {topic},",
        f"If you're tired of staying average in {topic},"
    ]

    identity = random.choice(identity_triggers)

    # Stronger emotional tension
    tension_bank = [
        "your actions don’t match your goals.",
        "you keep choosing comfort over growth.",
        "you say one thing but do another.",
        "you avoid what matters most.",
        "your habits are exposing you."
    ]

    tension = random.choice(tension_bank)

    resolution_bank = [
        "Growth begins when discomfort becomes normal.",
        "Consistency beats motivation every time.",
        "Discipline decides your future.",
        "Your identity shapes your destiny."
    ]

    resolution = random.choice(resolution_bank)

    cta_bank = [
        "Fix it today.",
        "Start acting differently.",
        "Decide who you want to become.",
        "Or stay the same."
    ]

    cta = random.choice(cta_bank)

    loop_line = random.choice([
        "Read that again.",
        "Let that sink in.",
        "Think about that.",
        "Now ask yourself why."
    ])

    if length == "short":
        full_script = f"{selected_hook} {resolution} {cta}"

    elif length == "medium":
        full_script = f"{selected_hook} {identity} {tension} {resolution} {cta} {loop_line}"

    else:
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
