from flask import Flask, request, jsonify
from flask_cors import CORS
import art
import json
import os
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# List of available styles (fonts) from the art library
available_styles = art.FONT_NAMES
scores_file = 'scores.json'
lock = threading.Lock()  # To ensure thread safety for file operations

# Initialize scores.json if it doesn't exist
if not os.path.exists(scores_file):
    with open(scores_file, 'w') as f:
        json.dump({style: 0 for style in available_styles}, f)

@app.route('/')
def home():
    return "Welcome to the ASCII Art Generator!"

@app.route('/styles', methods=['GET'])
def get_styles():
    return jsonify({'available_styles': available_styles})

@app.route('/ascii-art', methods=['POST'])
def generate_ascii_art():
    data = request.get_json()
    print(data)
    if not data or 'text' not in data or 'style' not in data:
        return jsonify({'error': 'Invalid request. Please provide text and style as JSON data'}), 400

    text = data['text']
    style = data['style']

    if style not in available_styles:
        return jsonify({'error': 'Invalid style. Please choose from /styles'}), 400

    try:
        ascii_art = art.text2art(text, font=style)
        update_score(style)
        return jsonify({'ascii_art': ascii_art})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_score(style):
    with lock:
        with open(scores_file, 'r+') as f:
            scores = json.load(f)
            scores[style] += 1
            f.seek(0)
            json.dump(scores, f)
            f.truncate()

@app.route('/scores', methods=['GET'])
def get_scores():
    with lock:
        with open(scores_file, 'r') as f:
            scores = json.load(f)
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
