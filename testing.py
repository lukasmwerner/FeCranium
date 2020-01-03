#! /usr/bin/python3
from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    return "We are online! Ayyy!"

@app.route('/open', methods=['POST'])
def open():
    print("opening...")
    return "Sucsess on opening!"

@app.route('/close', methods=['POST'])
def close():
    print("closing...")
    return "Sucsess on closing!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")