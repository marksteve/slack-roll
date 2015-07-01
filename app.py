import os
import random

import requests
from flask import Flask, json, request

random.seed()

app = Flask(__name__)


@app.route("/", methods=["POST"])
def roll():
  resp = ""
  dice = request.form["text"].split()
  for i, die in enumerate(dice):
    resp += "Dice {}\n".format(i + 1)
    rolls, faces = map(int, die.split("d"))
    for j in range(rolls):
      roll = random.randint(1, faces)
      resp += "  Roll {}: {}\n".format(j + 1, roll)
  icon_emoji = ":dice{}:".format(random.randint(1, 6))
  requests.post(
    os.environ["WEBHOOK_URL"],
    data=json.dumps({
      "text": resp,
      "icon_emoji": icon_emoji,
      "username": "Dice Roller",
      "channel": "#" + request.form["channel_name"],
    }),
    headers={"Content-Type": "application/json"},
  )
  return ""


app.run(host="0.0.0.0", port=os.environ["PORT"])
