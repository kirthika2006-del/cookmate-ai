# 🍳 Enna Samaikalam — Recipe Suggester Chatbot

Ingredients sonna, AI recipe suggest pannum chatbot. Flask + Gemini API use panni build panniruken.

## 📁 Folder Structure
```
enna-samaikalam/
├── app.py                 → Flask backend
├── chatbot_config.py      → Bot title + prompt (idha maathi vera bot-a maathalam)
├── templates/
│   └── index.html         → Chat UI
├── .env                   → API key (idha edit pannunga)
└── requirements.txt       → Python packages
```

## 🚀 Setup Steps (5 mins)

### 1. Gemini API Key eduthukonga
- [aistudio.google.com](https://aistudio.google.com) ku pogonga
- Google account la login pannunga
- "Get API Key" click pannunga → "Create API Key"
- Key-a copy pannikonga

### 2. `.env` file edit pannunga
`.env` file open pannitu, idha maathunga:
```
GEMINI_API_KEY=your_actual_key_here
```

### 3. Terminal la idha run pannunga
```bash
cd enna-samaikalam

# (Optional but recommended) Virtual environment create pannunga
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Packages install pannunga
pip install -r requirements.txt

# App run pannunga
python app.py
```

### 4. Browser la open pannunga
```
http://127.0.0.1:5000
```

Adhu than! Ingredients type panni test pannunga 🎉

## 🔧 Customize panna venuma?

Vera domain bot venum-na, `chatbot_config.py` la ரெண்டு variables mattum maathunga:
- `CHATBOT_TITLE` → bot peru
- `DOMAIN_DESCRIPTION_HINT` → bot enna panna venum nu prompt

Baaki code same-ah irukum, edhuvum maathanam venaam.

## ⚠️ Note
- `.env` file la real API key irundha, athை GitHub la public ah push pannadheenga
- Idhu single-user demo setup — multiple users same time use panna, session-based history venum
