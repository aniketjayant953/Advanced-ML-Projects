import paralleldots

paralleldots.set_api_key('z7Vl7DAdBbv6RF4YbLD9BJrmu9Pc2JfZtwprF7jqV4Y')


def ner(text):
    ner = paralleldots.ner(text)
    return ner


def sentiment(text):
    sent = paralleldots.sentiment(text)
    return sent


def abuse(text):
    ab = paralleldots.abuse(text)
    return ab
