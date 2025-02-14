from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/json')
def json_example():
    return jsonify(message="This is a JSON response")

if __name__ == "__main__":
    app.run(debug=FALSE)
