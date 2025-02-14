from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/json')
def json_example():
    return jsonify(message="This is a JSON response")

app.run(debug=True, port=5001)

