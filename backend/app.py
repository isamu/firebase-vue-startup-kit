#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/hello")
def hello():
    return jsonify(message='Hello, world!')

