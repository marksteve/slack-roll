import os
import random

from flask import Flask, request

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
  return resp


app.run(host="0.0.0.0", port=os.environ["PORT"])
