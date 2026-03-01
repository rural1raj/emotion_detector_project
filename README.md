# Emotion Detector

## Project Overview
Emotion Detector is a web application built with **Python** and **Flask** that analyzes the emotion expressed in a given text input. The application demonstrates the creation of a simple AI-based web application without using external NLP APIs.  

Users can enter text into the web interface, click "Analyze Emotion", and the app returns the predicted emotion with a formatted output.

---

## Features
- Analyze emotions from user-provided text.
- Simple and interactive web interface using Flask.
- Handles blank or invalid input gracefully.
- Modular structure with reusable Python functions.
- Unit tests included for core functionality.
- Styled web interface using CSS.



## Project Structure
motionDetector/
├── emotion_detection.py # Core emotion detection logic
├── server.py # Flask app for web deployment
├── templates/
│ └── index.html # HTML interface
├── static/
│ └── style.css # CSS styling
├── test_emotion_detection.py # Unit tests
└── init.py # Package initialization

python server.py
