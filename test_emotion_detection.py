import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(emotion_detector("I am so happy")["emotion"], "Happy")

    def test_sad(self):
        self.assertEqual(emotion_detector("I am very sad")["emotion"], "Sad")

    def test_neutral(self):
        self.assertEqual(emotion_detector("It is a book")["emotion"], "Neutral")

if __name__ == "__main__":
    unittest.main()