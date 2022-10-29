# Importing libraries
import os
import dash
import requests
import io
from dash import html
from dash import dcc
import pandas as pd
import plotly.graph_objs as go

# importing data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
download = requests.get(url).content
df_us = pd.read_csv(io.StringIO(download.decode('utf-8')))

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
download = requests.get(url).content
df_state = pd.read_csv(io.StringIO(download.decode('utf-8')))

def covid_cases():
    fig = go.Figure([go.Scatter(x = df_us['date'], y = df_us['cases'], line = dict(color = 'firebrick', width = 4))])
    fig.update_layout(title = 'COVID-19 cases in US', xaxis_title = 'Date', yaxis_title = 'Cases' )
    return fig

app = dash.Dash(__name__)
server = app.server
colors = {
    'background': '#afbddb',
    'text': '#0552f7'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children = [
html.H1(
        children='Covid Cases in US',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
        dcc.Graph(id = 'line_plot', figure = covid_cases())
    ]
)

if __name__ == '__main__':
    app.run_server()
