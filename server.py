"""
Flask server for the Emotion Detector application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def start_page():
    """
    Show the main page.

    Returns:
        index.html.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def analyze_emotions():
    """
    Runs emotion analyzer on customer text.

    Input:
        Customer inputs text into web page.

    Returns:
        Emotion detection analysis of the text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion = emotion_detector(text_to_analyze)
    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    customer_response = (
        f"For the given statement, the system response is 'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. "
        f"The dominant emotion is <b>{emotion['dominant_emotion']}<b>."
    )
    return customer_response

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
