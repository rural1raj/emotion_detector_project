from textblob import TextBlob

def emotion_detector(text):
    if not text.strip():
        return None
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        emotion = "Happy"
    elif polarity < -0.1:
        emotion = "Sad"
    else:
        emotion = "Neutral"
    return {"text": text, "emotion": emotion}