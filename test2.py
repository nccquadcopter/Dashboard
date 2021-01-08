import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
df = pd.read_csv("mag_data.csv") #put data file name here

#Sensor1
fig1 = px.line(df, x="sensor_time", y="magx", title='Sensor1')

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#Sensor2
fig2 = px.line(df, x="sensor_time", y="magy", title='Sensor2')

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#Sensor3
fig3 = px.line(df, x="sensor_time", y="magz", title='Sensor3')

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.H1(children='Data Visualization',
            style={
                'textAlign': 'center',
                'color': colors['text']
        }
    ),

    html.H2(children='Normandale\'s Quadcopter Team',
            style={
                'textAlign': 'center',
                'color': colors['text']
        }
    ),

    html.Div(children='Web application framework for data from the Blue Heron', 
            style={
                'textAlign': 'center',
                'color': colors['text']
        }
    ),

    #Graph for Sensor1
    dcc.Graph(
        id='sensor1_graph',
        figure=fig1
    ),

    #Graph for Sensor2
    dcc.Graph(
        id='sensor2_graph',
        figure=fig2
    ),

   dcc.Graph(
        id='sensor3_graph',
        figure=fig3
    )    
])

if __name__ == '__main__':
    app.run_server(debug=True)