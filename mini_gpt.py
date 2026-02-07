# mini_gpt.py
# Version avancée d’un mini modèle local pour répondre intelligemment
# quand l’API externe ne répond pas.

import random

# -----------------------------
# 1. Base de connaissances
# -----------------------------

INTENTS = {
    "greeting": {
        "keywords": ["bonjour", "salut", "hello", "yo", "coucou"],
        "responses": [
            "Salut ! Comment puis-je t’aider aujourd’hui ?",
            "Bonjour ! Tu veux faire quoi maintenant ?",
            "Hey ! Je suis là si tu as besoin."
        ]
    },

    "how_are_you": {
        "keywords": ["ça va", "comment tu vas", "tu vas bien"],
        "responses": [
            "Je vais super bien ! Et toi ?",
            "Toujours en pleine forme. Et toi, comment tu te sens ?",
            "Je suis opérationnel à 100%. Et toi ?"
        ]
    },

    "identity": {
        "keywords": ["qui es-tu", "tu es qui", "c'est quoi toi"],
        "responses": [
            "Je suis une IA locale, un mini modèle qui prend le relais si l’API externe ne répond pas.",
            "Je suis ton assistant local, conçu pour t’aider même hors connexion.",
            "Je suis une petite IA embarquée, prête à t’aider en cas de panne."
        ]
    },

    "help": {
        "keywords": ["aide", "help", "comment faire", "je comprends pas"],
        "responses": [
            "Je peux t’aider ! Explique-moi ce que tu veux faire.",
            "Je suis là pour t’aider. Dis-moi ce que tu veux accomplir.",
            "Pas de souci, je t’accompagne. Tu veux faire quoi exactement ?"
        ]
    },

    "joke": {
        "keywords": ["blague", "raconte une blague", "rigoler"],
        "responses": [
            "Pourquoi les programmeurs confondent Halloween et Noël ? Parce que OCT 31 = DEC 25.",
            "J’ai essayé d’écrire une blague sur l’IA… mais elle n’a pas été générée.",
            "Tu veux une blague ? Les bugs. Voilà."
        ]
    },

    "goodbye": {
        "keywords": ["au revoir", "bye", "à plus", "ciao"],
        "responses": [
            "À plus ! Reviens quand tu veux.",
            "Bye ! Je reste dans le coin.",
            "À bientôt !"
        ]
    }
}

# -----------------------------
# 2. Analyseur d’intentions
# -----------------------------

def detect_intent(message: str):
    message = message.lower()

    for intent, data in INTENTS.items():
        for kw in data["keywords"]:
            if kw in message:
                return intent

    return None  # aucune intention trouvée


# -----------------------------
# 3. Générateur de réponses
# -----------------------------

def generate_response(intent: str):
    if intent in INTENTS:
        return random.choice(INTENTS[intent]["responses"])
    return None


# -----------------------------
# 4. Réponse par défaut intelligente
# -----------------------------

def fallback_response(message: str):
    return (
        "Je ne suis pas sûr de comprendre, mais je suis là. "
        "Tu peux reformuler ou me dire ce que tu veux faire."
    )


# -----------------------------
# 5. Fonction principale
# -----------------------------

def local_answer(message: str) -> str:
    """
    IA locale avancée :
    - détecte l’intention
    - génère une réponse intelligente
    - utilise un fallback si rien ne correspond
    """

    intent = detect_intent(message)

    if intent:
        return generate_response(intent)

    return fallback_response(message)
