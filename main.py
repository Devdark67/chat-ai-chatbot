from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

app = FastAPI()

# Récupérer ta clé API depuis .env
EXTERNAL_API_KEY = os.getenv("EXTERNAL_API_KEY")

# URL et modèle OpenAI
EXTERNAL_API_URL = "https://api.openai.com/v1/chat/completions"
EXTERNAL_MODEL = "gpt-4o-mini"   # tu peux changer si besoin

# Format des messages envoyés par le frontend
class ChatRequest(BaseModel):
    message: str

# Fonction qui appelle l'API OpenAI
def call_llm(message: str):
    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": EXTERNAL_MODEL,
        "messages": [
            {"role": "system", "content": "Tu es un assistant utile, clair et intelligent."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(EXTERNAL_API_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]

# Route API appelée par ton frontend
@app.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message
    reply = call_llm(user_message)
    return {"reply": reply}
