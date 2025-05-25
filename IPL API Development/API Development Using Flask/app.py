from flask import Flask, jsonify, request
import ipl
import json
import jugaad

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1, team2)
    return response


@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team_name')
    response = jugaad.teamAPI(team_name)
    return response


@app.route('/api/batting-record')
def batsman_record():
    batsman = request.args.get('batsman')
    response = jugaad.batsmanAPI(batsman)
    return response


@app.route('/api/bowling-record')
def bowler_record():
    bowler = request.args.get('bowler')
    response = jugaad.batsmanAPI(bowler)
    return response


app.run(debug=True)
