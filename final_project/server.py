from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle empty input
    if not text_to_analyze:
        return "Error: No text provided for analysis."

    result = emotion_detector(text_to_analyze)

    # Handle possible errors from mock or API
    if not isinstance(result, dict) or "dominant_emotion" not in result:
        return "Error: Could not process the input."

    # Constructing the output string
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result.get('anger', 0)}, "
        f"'disgust': {result.get('disgust', 0)}, "
        f"'fear': {result.get('fear', 0)}, "
        f"'joy': {result.get('joy', 0)}, and "
        f"'sadness': {result.get('sadness', 0)}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    app.run(debug=True)
