import paralleldots


class API:
    def __init__(self):
        paralleldots.set_api_key('z7Vl7DAdBbv6RF4YbLD9BJrmu9Pc2JfZtwprF7jqV4Y')

    def sentiment_analysis(self, text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self, text):
        response = paralleldots.ner(text)
        return response

    def emotion_analysis(self, text):
        response = paralleldots.emotion(text)
        return response
