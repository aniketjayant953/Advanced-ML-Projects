import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    # list has to be copied like this
    text = y[:]
    y.clear()

    stw = stopwords.words('english')
    punct = string.punctuation

    for i in text:
        if i not in stw and i not in punct:
            y.append(i)

    text = y[:]
    y.clear()

    lemma = WordNetLemmatizer()

    for i in text:
        y.append(lemma.lemmatize(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area('Enter the Message')

if st.button('Predict'):
    # 1. Preprocess

    transformed_sms = transform_text(input_sms)

    # 2. Vectorize

    vector_input = tfidf.transform([transformed_sms])

    # 3. predict
    result = model.predict(vector_input)[0]

    # 4. Display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
