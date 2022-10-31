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
#url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
#download = requests.get(url).content
#df_us = pd.read_csv(io.StringIO(download.decode('utf-8')))

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
download = requests.get(url).content
df_state = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Getting recent numbers
yesterday = date.today() - timedelta(1)
df_state = df_state[df_state.date == str(yesterday)]

# Getting states abbrevations
states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

df_state['state_ab'] = df_state['state'].map(states)


def covid_cases():
    fig = px.line(x = df_us['date'], y = df_us['cases'])
    fig.update_layout(title = 'COVID-19 cases in US', xaxis_title = 'Date', yaxis_title = 'Cases' )
    return fig

def states_map():
    fig = px.choropleth(df_state, color="cases", locationmode = 'USA-states', locations = 'state_ab', scope = 'usa')
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
        #dcc.Graph(id = 'line_plot', figure = covid_cases()),
        dcc.Graph(id = 'map', figure = states_map())
        ]
)

if __name__ == '__main__':
    app.run_server()
