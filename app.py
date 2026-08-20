# ============================================
# app.py
# Flask backend for "Enna Samaikalam" chatbot
# ============================================

import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from google import genai
from google.genai import types

from chatbot_config import CHATBOT_TITLE, DOMAIN_DESCRIPTION_HINT

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found! Please add it to your environment variables."
    )

# New Google GenAI client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        chatbot_title=CHATBOT_TITLE
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=DOMAIN_DESCRIPTION_HINT
            )
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Gemini API Error: {e}")
        return jsonify({
            "error": "Gemini API request failed"
        }), 500


@app.route("/reset", methods=["POST"])
def reset():
    return jsonify({"status": "Chat history reset"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print(f"\n🍳 {CHATBOT_TITLE} is starting...")
    print(f"👉 Open http://127.0.0.1:{port} in your browser\n")

    app.run(
        debug=False,
        host="0.0.0.0",
        port=port
    )