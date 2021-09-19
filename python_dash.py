import dash
import os
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import csv
import tempfile
import datetime
from datetime import date


#retrieve data from github url
url ="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

#create a yesterday's date string to use in the new csv file
today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
yesterday_to_string = str(yesterday)

#modify data in a new csv file to show only the latest date

dff = pd.read_csv(url)
dff[(dff['date'] == yesterday_to_string)].to_csv("data1/temp.csv", index=False)


with open("data1/temp.csv", newline='') as File:  
    reader = csv.reader(File)


with open("data1/temp.csv", 'r') as inp, open("data1/updated_data.csv", 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[1] != '':
            writer.writerow(row)

app = dash.Dash(external_stylesheets=[dbc.themes.LUMEN])
server = app.server

df = pd.read_csv("data1/updated_data.csv")


#Continent csv files
with open("data1/temp.csv", 'r') as inp1, open("data1/asia.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'Asia' or row1[1] == 'continent':
            writer1.writerow(row1)
with open("data1/temp.csv", 'r') as inp1, open("data1/africa.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'Africa' or row1[1] == 'continent':
            writer1.writerow(row1)
with open("data1/temp.csv", 'r') as inp1, open("data1/europe.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'Europe' or row1[1] == 'continent':
            writer1.writerow(row1)
with open("data1/temp.csv", 'r') as inp1, open("data1/north.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'North America' or row1[1] == 'continent':
            writer1.writerow(row1)
with open("data1/temp.csv", 'r') as inp1, open("data1/south.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'South America' or row1[1] == 'continent':
            writer1.writerow(row1)
with open("data1/temp.csv", 'r') as inp1, open("data1/oceania.csv", 'w') as out1:
    writer1 = csv.writer(out1)
    for row1 in csv.reader(inp1):
        if row1[1] == 'Oceania' or row1[1] == 'continent':
            writer1.writerow(row1)


asia = pd.read_csv("data1/asia.csv")
africa = pd.read_csv("data1/africa.csv")
europe = pd.read_csv("data1/europe.csv")
north = pd.read_csv("data1/north.csv")
south = pd.read_csv("data1/south.csv")
oceania = pd.read_csv("data1/oceania.csv")
#map and graphs plotting

map_cases = px.choropleth(df, locations="iso_code",
                    color="total_cases", # lifeExp is a column of gapminder
                    hover_name="location", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
#map_cases.update_layout(margin=dict(l=0, r=0, t=60, b=60),paper_bgcolor="steelblue")

map_deaths = px.choropleth(df, locations="iso_code",
                    color="total_deaths", # lifeExp is a column of gapminder
                    hover_name="location", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
#map_deaths.update_layout(margin=dict(l=0, r=0, t=60, b=60),paper_bgcolor="steelblue")

map_new_cases = px.choropleth(df, locations="iso_code",
                    color="new_cases", # lifeExp is a column of gapminder
                    hover_name="location", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
#map_cases.update_layout(margin=dict(l=0, r=0, t=60, b=60),paper_bgcolor="steelblue")

map_new_deaths = px.choropleth(df, locations="iso_code",
                    color="new_deaths", # lifeExp is a column of gapminder
                    hover_name="location", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
#map_deaths.update_layout(margin=dict(l=0, r=0, t=60, b=60),paper_bgcolor="steelblue")



chart_cases = px.sunburst(df, path=['continent', 'location'], values='total_cases',
                  color='total_cases', hover_data=['iso_code'])

chart_deaths = px.sunburst(df, path=['continent', 'location'], values='total_deaths',
                  color='total_deaths', hover_data=['iso_code'])

tree_cases = fig = px.treemap(df, path=[px.Constant('world'), 'continent', 'location'], values='total_cases',
                  color='total_cases', hover_data=['iso_code'])

tree_deaths = fig = px.treemap(df, path=[px.Constant('world'), 'continent', 'location'], values='total_deaths',
                  color='total_deaths', hover_data=['iso_code'])


stats_asia = fig = px.bar(asia, y='new_cases', x='location')
stats_asia.update_traces(texttemplate='%{text:.2s}', textposition='outside')
stats_asia.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
stats_africa = fig = px.bar(africa, y='new_cases', x='location')
stats_africa.update_traces(texttemplate='%{text:.2s}', textposition='outside')
stats_africa.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
stats_europe = fig = px.bar(europe, y='new_cases', x='location')
stats_europe.update_traces(texttemplate='%{text:.2s}', textposition='outside')
stats_europe.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
stats_north = fig = px.bar(north, y='new_cases', x='location')
stats_north.update_traces(texttemplate='%{text:.2s}', textposition='outside')
stats_north.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
stats_south = fig = px.bar(south, y='new_cases', x='location')
stats_south.update_traces(textposition='outside')
stats_south.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
stats_oceania = fig = px.bar(oceania, y='new_cases', x='location')
stats_oceania.update_traces(textposition='outside')
stats_oceania.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')



SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Dash Data", className="display-5"),
        html.Hr(),
        html.P(
            "Select the data you want to check in the dashboard", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Covid-19 Total Cases", href="/total_cases", active="exact"),
                dbc.NavLink("Covid-19 Total Deaths", href="/total_deaths", active="exact"),
                dbc.NavLink("Daily Cases and Deaths", href="/daily", active="exact"),
                dbc.NavLink("Continents", href="/continents", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


#Plots for each page

total_cases = html.Div(children=[

    html.Center(children='''
        Data representations of total Covid-19 cases in the world
    ''',className="display-3"),
    html.Center(children='''
        Latest date: {}
    '''.format(yesterday_to_string),className="display-5"),

    dcc.Graph(
        id='map_cases',
        figure=map_cases
    ),

    dcc.Graph(
        id='chart_cases',
        figure=chart_cases
    ),

    dcc.Graph(
        id='tree_cases',
        figure=tree_cases
    )



])

total_deaths = html.Div(children=[


    html.Center(children='''
        Data representations of total Covid-19 deaths in the world
    ''',className="display-3"),

    html.Center(children='''
        Latest date: {}
    '''.format(yesterday_to_string),className="display-5"),

    dcc.Graph(
        id='map_deaths',
        figure=map_deaths
    ),

    dcc.Graph(
        id='chart_deaths',
        figure=chart_deaths
    ),

    dcc.Graph(
        id='tree_deaths',
        figure=tree_deaths
    )
])

new_cases = html.Div(children=[


    html.Center(children='''
        Data representations of daily Covid-19 cases in the world
    ''',className="display-3"),
    html.Center(children='''
        Latest date: {}
    '''.format(yesterday_to_string),className="display-5"),

    dcc.Graph(
        id='map_new_cases',
        figure=map_new_cases
    ),
])

new_deaths = html.Div(children=[


    html.Center(children='''
        Data representations of daily Covid-19 deaths in the world
    ''',className="display-3"),

    dcc.Graph(
        id='map_new_deaths',
        figure=map_new_deaths
    ),

])

stats = html.Div(children=[


    html.Center(children='''
       New Cases In Asia
    ''',className="display-3"),

    dcc.Graph(
        id='asia',
        figure=stats_asia
    ),
    html.Center(children='''
       New Cases In Africa
    ''',className="display-3"),

    dcc.Graph(
        id='africa',
        figure=stats_africa
    ),
    html.Center(children='''
       New Cases In Europe
    ''',className="display-3"),

    dcc.Graph(
        id='europe',
        figure=stats_europe
    ),
    html.Center(children='''
       New Cases In North America
    ''',className="display-3"),

    dcc.Graph(
        id='north',
        figure=stats_north
    ),
    html.Center(children='''
       New Cases In South America
    ''',className="display-3"),

    dcc.Graph(
        id='south',
        figure=stats_south
    ),
    html.Center(children='''
       New Cases In Oceania
    ''',className="display-3"),

    dcc.Graph(
        id='oceania',
        figure=stats_oceania
    ),

])

home = dbc.Container(
    [
        html.Center("Covid-19 Data Visualization", className="bg-primary text-white display-3"),
        html.P(
            ''' This is a small experimental project using Python Dash and Plotly to visualize the total Covid-19 cases in the form of a
            world map, pie chart or treemap. The project is in initial phases and it will serve as a template for other data visualizations
            and experiments. The data are in csv files and the plan is to switch to JSON or to get data using APIs for quicker results and less storage. The initial idea of the project is to get the csv
            data from Github repos and pass the data that you actually want into a local csv file, which will be used in the maps and graphs. The data are updated
            daily in the repository, so there is no need to worry about modifying data yourself. I have used Plotly maps and graphs, which are interactive and
            quick to build. Note that it might get some time to load the data, depending on the internet connection.''',
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            '''The .csv files are taken from OWID's (Our World In Data) Github repository. In order to check them, please click the "OWID" button. 
            To know me better, please click the "About Me" button'''
        ),
        html.P(dbc.Button("OWID", color="primary",href="https://github.com/owid/covid-19-data"), className="lead"),
        html.P(dbc.Button("About Me", color="primary",href="https://kev-s-personal.herokuapp.com"), className="lead"),
    ],
    fluid=True,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home
    elif pathname == "/total_cases":
        return total_cases
    elif pathname == "/total_deaths":
        return total_deaths
    elif pathname == "/daily":
        return new_cases, new_deaths
    elif pathname == "/continents":
        return stats
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)
    