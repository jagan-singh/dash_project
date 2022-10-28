# Importing libraries
import os
import dash
import requests
import io
import dash_core_components as dcc
import dash_html_components as html
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
app.layout = html.Div(style={'backgroundColor': colors['background']}, children = [
        dcc.Graph(id = 'line_plot', figure = covid_cases())    
    ]
)

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
