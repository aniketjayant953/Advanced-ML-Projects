import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc
import dash

data = pd.read_csv('gap.csv')

print(data.head())

app = dash.Dash()
# for heading
# app.layout = html.H1(children='My First Dashboard',style={'color':'red', 'text-align':'center'})

app.layout = html.Div([
    html.Div(children=[
        html.H1('My First Dashboard', style={'color': 'red', 'text-align': 'center'})
    ], style={'border': '1px black solid', 'float': 'left', 'width': '100%', 'height': '70px'}),
    html.Div(children=[
        dcc.Graph(id='scatter-plot',
                  figure={'data': [go.Scatter(x=data['pop'],
                                              y=data['gdpPercap'],
                                              mode='markers')],
                          'layout': go.Layout(title='Scatter Plot')})
    ], style={'border': '1px black solid', 'float': 'left', 'width': '49.9%'}),
    html.Div(children=[
        dcc.Graph(id='box-plot',
                  figure={'data': [go.Box(x=data['gdpPercap'])],
                          'layout': go.Layout(title='Boxplot')})
    ], style={'border': '1px black solid', 'float': 'left', 'width': '49.7%' })
])
if __name__ == '__main__':
    app.run(debug=True)

