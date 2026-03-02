from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector Running"

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze.strip() == "":
        return "Invalid input! Please enter some text."

    result = emotion_detector(text_to_analyze)

    return str(result)

if __name__ == "__main__":
    app.run()
