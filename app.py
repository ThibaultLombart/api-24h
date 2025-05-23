from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text-generation", model="distilgpt2")

@app.route("/generate", methods=["POST"])
def generate_poem():
    data = request.get_json()
    prompt = data.get("prompt", "Écris un poème sur Lyon et ses lumières :")
    result = generator(prompt, max_new_tokens=80, temperature=0.9, top_k=50)
    return jsonify(result[0])  # contient 'generated_text'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
