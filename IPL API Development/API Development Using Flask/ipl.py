import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)



def teamsAPI():
    teams = list(matches['Team1'].unique())
    teams_dict = {
        'teams': teams
    }
    return teams_dict


def teamVteamAPI(team1, team2):
    temp_df = matches[((matches['Team1'] == team1) & (matches["Team2"] == team2)) | ((matches['Team2'] == team1) & (matches["Team1"] == team2))]
    teams = list(matches['Team1'].unique())
    if team1 in teams and team2 in teams:

        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'total_matches': str(total_matches),
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            'draws': str(draws)
        }

        return response
    else:
        return {'message':'teams not found'}