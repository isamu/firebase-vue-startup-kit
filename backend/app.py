#!/usr/bin/env python3
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import openai
import os

# Configuration
load_dotenv() # Load default environment variables (.env)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL", "gpt-3.5-turbo")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", 0.7))
assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get('name')
    return f"<p>Hello, {name or 'World'}!</p>"

@app.route("/api/chat")
def hello():
    messages = []
    query = request.args.get('query')
    messages.append({"role":"user", "content":query or "Hello."})
    response = openai.ChatCompletion.create(model=OPENAI_API_MODEL, messages=messages, temperature=OPENAI_TEMPERATURE)
    return jsonify(response['choices'][0]['message'])

if (__name__ == '__main__'):
    app.run(port=8081)