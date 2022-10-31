# Importing libraries
import os
import dash
import requests
import io
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

# importing data
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
download = requests.get(url).content
df_us = pd.read_csv(io.StringIO(download.decode('utf-8')))

url = "https://raw.githubusercontent.com/jagansingh93/covid_data/main/Weekly_United_States_COVID-19_Cases_and_Deaths_by_State.csv"
download = requests.get(url).content
df_state = pd.read_csv(io.StringIO(download.decode('utf-8')))
df_state.loc[df_state.new_cases  < 0,'new_cases'] = df_state.loc[df_state.new_cases  < 0,'new_cases'].abs()

def covid_cases():
    fig = px.line(x = df_us['date'], y = df_us['cases'])
    fig.update_layout(title = 'COVID-19 cases in US', xaxis_title = 'Date', yaxis_title = 'Cases' )
    return fig

def states_map():
    fig = px.scatter_geo(df_state, size="new_cases", locationmode = 'USA-states', locations = 'state', scope = 'usa', animation_frame = 'date_updated')
    fig.update_layout(title = 'States map')
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
        dcc.Graph(id = 'line_plot', figure = covid_cases()),
        dcc.Graph(id = 'map', figure = states_map())
        ]
)

if __name__ == '__main__':
    app.run_server()
