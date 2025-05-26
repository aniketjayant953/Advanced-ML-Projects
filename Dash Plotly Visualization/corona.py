import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc
import dash
from dash.dependencies import Input, Output

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
covid = pd.read_csv('covid_19_india.csv')
age = pd.read_csv('AgeGroupDetails.csv')
patients = pd.read_csv('IndividualDetails.csv')
total = patients.shape[0]
active = patients[patients['current_status'] == 'Hospitalized'].shape[0]
recovered = patients[patients['current_status'] == 'Recovered'].shape[0]
deceased = patients[patients['current_status'] == 'Deceased'].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('CoronaVirus Pandemic', style={'color': 'white', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', className='text-light'),
                    html.H3(total, className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases', className='text-light'),
                    html.H3(active, className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered Cases', className='text-light'),
                    html.H3(recovered, className='text-light')
                ], className='card-body')
            ], className='card bg-warning')
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Deaths', className='text-light'),
                    html.H3(deceased, className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='line',
                              figure={'data': [go.Scatter(x=covid['Date'],
                                                       y=covid['Confirmed'], mode='lines')],
                                      'layout': go.Layout(title='Day By Day Cases')})
                ])
            ])
        ], className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='pie',
                              figure={'data': [go.Pie(labels=age['AgeGroup'],
                                                       values=age['TotalCases'])],
                                      'layout': go.Layout(title='Age Distribution')})
                ])
            ])
        ], className='col-md-6')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row')
], className='container')


@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_graph(type):
    if type == 'All':
        pbar = patients['detected_state'].value_counts().reset_index()

        return {'data': [go.Bar(x=pbar.iloc[:, 0], y=pbar.iloc[:, 1])],
                'layout': go.Layout(title='State Total Count')}

    else:
        npat = patients[patients['current_status'] == type]
        pbar = npat['detected_state'].value_counts().reset_index()

        return {'data': [go.Bar(x=pbar.iloc[:, 0], y=pbar.iloc[:, 1])],
                'layout': go.Layout(title='State Total Count')}


if __name__ == '__main__':
    app.run(debug=True)
