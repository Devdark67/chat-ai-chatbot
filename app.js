// Sélection des éléments
const chat = document.getElementById("chat");
const msg = document.getElementById("msg");
const sendBtn = document.getElementById("send-btn");

// Fonction pour ajouter un message dans le chat
function addMessage(text, sender) {
  const p = document.createElement("p");
  p.textContent = (sender === "user" ? "🧑‍💻 " : "🤖 ") + text;
  chat.appendChild(p);
  chat.scrollTop = chat.scrollHeight;
}

// Fonction pour envoyer le message au backend
async function sendMessage() {
  const text = msg.value.trim();
  if (!text) return;

  addMessage(text, "user");
  msg.value = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });

    const data = await response.json();
    addMessage(data.reply, "bot");

  } catch (error) {
    addMessage("Erreur : impossible de contacter le serveur.", "bot");
  }
}

// Envoi avec le bouton
sendBtn.addEventListener("click", sendMessage);

// Envoi avec la touche Entrée
msg.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});
