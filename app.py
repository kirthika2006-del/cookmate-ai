# ============================================
# app.py
# Flask backend for "Enna Samaikalam" chatbot
# ============================================

import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

from chatbot_config import CHATBOT_TITLE, DOMAIN_DESCRIPTION_HINT

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found! Please add it to your .env file.\n"
        "Get a free key from https://aistudio.google.com"
    )

genai.configure(api_key=API_KEY)

# Initialize the Gemini model with our system instruction (domain prompt)
model = genai.GenerativeModel(
    model_name="gemini-3.6-flash",
    system_instruction=DOMAIN_DESCRIPTION_HINT
)

app = Flask(__name__)

# In-memory chat history store (per server run — resets on restart)
# For multiple users at once, you'd key this by session ID.
chat_session = model.start_chat(history=[])


@app.route("/")
def home():
    return render_template("index.html", chatbot_title=CHATBOT_TITLE)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = chat_session.send_message(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500


@app.route("/reset", methods=["POST"])
def reset():
    global chat_session
    chat_session = model.start_chat(history=[])
    return jsonify({"status": "Chat history reset"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🍳 {CHATBOT_TITLE} is starting...")
    print(f"👉 Open http://127.0.0.1:{port} in your browser\n")
    app.run(debug=False, host="0.0.0.0", port=port)