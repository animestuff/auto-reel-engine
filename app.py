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
    return prefix + f"{topic.capitalize()} shapes your future. Act now."

elif length == "medium":
    return prefix + f"You say you want success in {topic}, but your habits say otherwise. Discipline creates results. Fix your focus."

elif length == "long":
    return prefix + f"Most people blame {topic} for their failures. But the truth is, growth begins when you stop avoiding discomfort. Master your habits. Control your emotions. Build discipline daily."

else:
    return prefix + f"{topic.capitalize()} determines your direction. Choose wisely."

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

return jsonify({
    "script": script,
    "topic": topic,
    "length": length,
    "tone": tone
})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
