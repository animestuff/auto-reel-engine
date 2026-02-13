from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


def generate_script(topic, length, tone):
    if tone == "aggressive":
        prefix = "Listen carefully. "
    elif tone == "calm":
        prefix = "Think about this. "
    elif tone == "dark":
        prefix = "Here’s the uncomfortable truth. "
    elif tone == "luxury":
        prefix = "High performers understand this. "
    else:
        prefix = ""

   if length == "short":
       hook = prefix + f"{topic.capitalize()} shapes your future."
       body = "Your habits decide your results."
       cta = "Act now."
   elif length == "medium":
       hook = prefix + f"You say you want success in {topic}."
       body = "But your habits say otherwise. Discipline creates results."
       cta = "Fix your focus."
   elif length == "long":
       hook = prefix + f"Here’s the uncomfortable truth."
       body = f"Most people blame {topic} for their failures. But growth begins when you stop avoiding discomfort."
       cta = "Master your habits."
   else:
       hook = prefix + f"{topic.capitalize()} determines your direction."
       body = "Choose wisely."
       cta = "Start today."

   full_script = f"{hook} {body} {cta}"

   return {
     "hook": hook,
     "body": body,
     "cta": cta,
     "full_script": full_script,
     "hashtags": [f"#{topic}", "#discipline", "#mindset"]
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
