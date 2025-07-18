import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    api_key = "your-api-key"
    url = "your-api-url"

    headers = {'Content-Type': 'application/json'}
    params = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }

    response = requests.post(
        url + "/v1/analyze?version=2021-08-01",
        auth=("apikey", api_key),
        headers=headers,
        json=params
    )

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = response.json()["emotion"]["document"]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions
