"""
server.py
"""
from flask import Flask
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_handler():
    # return g.data
    with open("data.json", "r", encoding="utf-8") as f:
        string = f.read()

    return string


if __name__ == "__main__":
    app.run()
