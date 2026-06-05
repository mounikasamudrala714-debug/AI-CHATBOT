from flask import Flask, render_template, request, jsonify
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(
    __name__,
    template_folder=FRONTEND_DIR,
    static_folder=FRONTEND_DIR,
    static_url_path="/static"
)

def get_bot_reply(user_message):
    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Nice to meet you."
    elif "name" in message:
        return "My name is Simple Python Chatbot."
    elif "internship" in message:
        return "This chatbot is a simple internship project made using Python and Flask."
    elif "features" in message:
        return "My features are chatting with users, giving replies, and running in a browser."
    elif "help" in message:
        return "You can ask me about my name, features, or internship project."
    elif "bye" in message:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I do not understand that yet. Please ask something else."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_bot_reply(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host="127.0.0.1", port=5000)