import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Sample Data (replace with your own data loading)
df = pd.read_csv('https://reyazahmad7045-max')

# Initialize the Dash app
# external_stylesheets can be used for styling, e.g., dbc.themes.BOOTSTRAP
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Gapminder Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.P("Select Year:"),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in df['year'].unique()],
            value=df['year'].min(), # Default value
            clearable=False
        ),
    ], style={'width': '50%', 'margin': 'auto'}),

    dcc.Graph(id='display-graph')
])

# Callback to update the graph based on dropdown selection
@app.callback(
    Output('display-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_graph(selected_year):
    filtered_df = df[df['year'] == selected_year]
    fig = px.scatter(
        filtered_df, 
        x="gdpPercap", 
        y="lifeExp", 
        size="pop", 
        color="continent", 
        hover_name="country", 
        log_x=True, 
        size_max=60,
        title=f"Life Expectancy vs GDP per Capita in {selected_year}"
    )
    return fig

# Run the app
if __name__ == '__main__':
    # Run the server on http://127.0.0.1
    app.run_server(debug=True)
