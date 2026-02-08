import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]["emotion"]
        emotion = {
            'anger' : emotions["anger"],
            'disgust' : emotions["disgust"],
            'fear' : emotions["fear"],
            'joy' : emotions["joy"],
            'sadness' : emotions["sadness"],
            'dominant_emotion' : max(emotions, key=emotions.get)
        }
    elif response.status_code == 400:
        emotion = {
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness' : None,
            'dominant_emotion' : None
        }
    return emotion
    
