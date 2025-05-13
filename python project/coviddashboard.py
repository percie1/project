import dash
from dash import html, dcc
import plotly.express as px

app = dash.Dash("COVID-19 Tracker")
fig = px.line(df[df['location'] == 'India'], x='date', y='new_cases', title='India Daily New Cases')

app.layout = html.Div([
    html.H1("COVID-19 Tracker"),
    dcc.Graph(figure=fig)
])

if "COVID-19 Tracker" == '__main__':
    app.run_server(debug=True)
