from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import random

def generate_script(topic, length, tone, intensity):

    topic_cap = topic.capitalize()

    # ==================================================
    # EMOTION FOUNDATION (Human, lived experience)
    # ==================================================

    emotion_engine = {

        "joy": {
            "identity": f"When {topic} finally starts working,",
            "tension": "you realize it was never about motivation.",
            "resolution": f"{topic_cap} was about standards."
        },

        "sadness": {
            "identity": f"When you fail at {topic},",
            "tension": "it hits deeper than you admit.",
            "resolution": f"{topic_cap} forces you to rebuild quietly."
        },

        "anger": {
            "identity": f"If you're frustrated with your {topic},",
            "tension": "that frustration is telling you something.",
            "resolution": f"{topic_cap} doesn't reward half effort."
        },

        "fear": {
            "identity": f"If {topic} scares you,",
            "tension": "it's because growth requires loss.",
            "resolution": f"{topic_cap} demands a different version of you."
        },

        "disgust": {
            "identity": f"If you're disappointed in your effort around {topic},",
            "tension": "that's self-awareness waking up.",
            "resolution": f"{topic_cap} changes when standards change."
        },

        "anticipation": {
            "identity": f"If you feel something bigger waiting in {topic},",
            "tension": "that pull isn't random.",
            "resolution": f"{topic_cap} responds to preparation."
        },

        "broken": {
            "identity": f"When {topic} feels impossible,",
            "tension": "usually you're fighting yourself, not the goal.",
            "resolution": f"{topic_cap} starts when excuses stop."
        },

        "admiration": {
            "identity": f"When you admire someone strong in {topic},",
            "tension": "you're seeing who you could become.",
            "resolution": f"{topic_cap} belongs to the disciplined."
        }

    }

    selected_emotion = random.choice(list(emotion_engine.keys()))
    emotion_block = emotion_engine[selected_emotion]

    identity = emotion_block["identity"]
    tension = emotion_block["tension"]
    resolution = emotion_block["resolution"]

    # ==================================================
    # INTENSITY LAYER (Emotional force)
    # ==================================================

    if intensity == "low":
        tension += " And that’s okay."
        cta = "Take one small step."

    elif intensity == "medium":
        tension += " You already know it."
        cta = "Be consistent."

    elif intensity == "high":
        tension += " Stop pretending you don't see it."
        cta = "Fix it now."

    else:  # extreme
        tension += " You’re not confused. You’re avoiding it."
        cta = "Decide who you are."

    # ==================================================
    # TONE LAYER (Voice personality)
    # ==================================================

    if tone == "brutal":
        hook = random.choice([
            "Let’s stop lying to ourselves.",
            "You don’t need motivation. You need truth.",
            "Nobody owes you softness."
        ])

    elif tone == "calm":
        hook = random.choice([
            "Let’s talk honestly.",
            "Pause for a moment.",
            "Think about this carefully."
        ])

    elif tone == "elite":
        hook = random.choice([
            "High performers understand this.",
            "The disciplined see this early.",
            "Winners move differently for a reason."
        ])

    elif tone == "criminal":
        hook = random.choice([
            "The streets teach this fast.",
            "Pressure exposes who you are.",
            "Survival doesn't care about excuses."
        ])

    else:  # adult
        hook = random.choice([
            "After enough life, you see patterns.",
            "Experience teaches this eventually.",
            "Nobody explains this early enough."
        ])

    # ==================================================
    # LOOP TRIGGER (Replay value)
    # ==================================================

    loop_line = random.choice([
        "Read that again.",
        "Let that settle.",
        "Be honest with yourself.",
        "Sit with that for a second."
    ])

    # ==================================================
    # STRUCTURE (Natural rhythm)
    # ==================================================

    if length == "short":
        full_script = f"{hook} {resolution} {cta}"

    elif length == "medium":
        full_script = f"{hook} {identity} {tension} {resolution} {cta} {loop_line}"

    else:
        full_script = f"{hook} {identity} {tension} {resolution} {cta} {loop_line}"

    hashtags = list(set([
        f"#{topic.lower()}",
        "#mindset",
        "#growth",
        "#selfawareness",
        "#discipline"
    ]))

    return {
        "emotion": selected_emotion,
        "hook": hook,
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
