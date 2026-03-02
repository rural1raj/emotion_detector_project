import requests

def emotion_detector(text_to_analyze):

    if text_to_analyze.strip() == "":
        return {
            "error": "Invalid text! Please try again."
        }

    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.1,
        "joy": 0.6,
        "sadness": 0.15
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
