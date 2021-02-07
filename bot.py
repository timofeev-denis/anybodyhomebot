import requests
from emoji import emojize
from flask import Flask, request, jsonify, session

application = Flask(__name__)
application.config["SECRET_KEY"] = "secret"


@application.route("/", methods=["POST"])
def receive_update():
    cake = emojize(":cake:", use_aliases=True)
    pretzel = emojize(":pretzel:")
    chat_id = request.json["message"]["chat"]["id"]
    if "latest_message" in session:
        print("Previous message was " + session["latest_message"])
    else:
        print("Starting new session")
    session["latest_message"] = request.json["message"]["text"]

    send_message(chat_id, cake + pretzel + " " + request.json["message"]["text"] + "🐧")
    return jsonify(ok=True)


def send_message(chat_id, text):
    with open("bot_token.txt", "r+") as file:
        token = file.read()
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
