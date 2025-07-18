def emotion_detector(text_to_analyze):
    if "glad" in text_to_analyze:
        return {"dominant_emotion": "joy"}
    elif "mad" in text_to_analyze:
        return {"dominant_emotion": "anger"}
    elif "disgusted" in text_to_analyze:
        return {"dominant_emotion": "disgust"}
    elif "sad" in text_to_analyze:
        return {"dominant_emotion": "sadness"}
    elif "afraid" in text_to_analyze:
        return {"dominant_emotion": "fear"}
    else:
        return {"dominant_emotion": "neutral"}
