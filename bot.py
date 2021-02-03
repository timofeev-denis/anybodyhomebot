import requests
from emoji import emojize
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_update():
    cake = emojize(":cake:", use_aliases=True)
    pretzel = emojize(":pretzel:")
    if request.method == "POST":
        print(request.json)
    chat_id = request.json["message"]["chat"]["id"]
    send_message(chat_id, cake + pretzel + " " + request.json["message"]["text"] + "🐧")
    return jsonify(ok=True)


def send_message(chat_id, text):
    token = "1675723385:AAEJxiN5zQMmddupcjcUk7YkRFUWb_TTQlM"
    method = "sendMessage"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
