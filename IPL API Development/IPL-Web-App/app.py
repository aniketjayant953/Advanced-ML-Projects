from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('index.html', teams=sorted(teams))


@app.route('/teamvteam')
def team_v_team():
    try:
        team1 = request.args.get('team1')
        team2 = request.args.get('team2')

        response = requests.get(f'http://127.0.0.1:5000/api/teamvteam?team1={team1}&team2={team2}')
        response = response.json()

        response1 = requests.get('http://127.0.0.1:5000/api/teams')
        teams = response1.json()['teams']

        return render_template('index.html', result=response, teams=sorted(teams))
    except Exception as e:
        return render_template('error.html')


app.run(debug=True, port=8000)
