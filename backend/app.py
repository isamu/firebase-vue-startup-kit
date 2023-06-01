#!/usr/bin/env python3
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import openai
import os

# Configuration
load_dotenv() # Load default environment variables (.env)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"

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