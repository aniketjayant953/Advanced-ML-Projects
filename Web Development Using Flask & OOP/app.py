from flask import Flask, render_template, request, session, redirect
from db import Database
import api

# Visit nlpcloud.com and renew your api-key then it'll work.
# OOP project .ipynb file has all the code

app = Flask(__name__)

dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration Successful. Kindly Login.')
    else:
        return render_template('register.html', message='Email Already Exists')


@app.route('/perform_login', methods=['post'])
def perform_login():
    password = request.form.get('password')
    email = request.form.get('email')

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect email/password')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)

    txt = []
    for i in response['entities']:
        txt.append('Name-> ' + i['name'] + ',  ' + 'Category->' + str(i['category']))

    return render_template('ner.html', message=txt)


@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')


@app.route('/perform_sentiment', methods=['post'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = api.sentiment(text)
    print(response)

    txt = []
    for i in response['sentiment']:
        txt.append(i + '->' + str(response['sentiment'][i]))

    return render_template('sentiment.html', message=txt)


@app.route('/abuse')
def abuse():
    return render_template('abuse.html')


@app.route('/perform_abuse', methods=['post'])
def perform_abuse():
    text = request.form.get('abusive_text')
    response = api.abuse(text)
    print(response)

    txt = []
    for i in response:
        txt.append((i, response[i]))

    print(txt)

    return render_template('abuse.html', message=txt)


app.run(debug=True)
