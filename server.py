from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/analyze", methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    result = emotion_detector(text)
    if not result:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)