#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get('name')
    return f"<p>Hello, {name or 'World'}!</p>"

@app.route("/api/hello")
def hello():
    return jsonify(message='Hello, world!')

if (__name__ == '__main__'):
    app.run(port=8081)