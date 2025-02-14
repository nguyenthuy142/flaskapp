from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import socket

app = Flask(__name__)
app.secret_key = 'your_secret_key'

if __name__ == '__main__':
    app.run(debug=True)
