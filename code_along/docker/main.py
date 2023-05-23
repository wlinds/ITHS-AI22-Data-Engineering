import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import random

app = Dash(__name__)

dropdown_options = [
    {"label": "10", "value": 10},
    {"label": "100", "value": 100},
    {"label": "100,000", "value": 100_000}
]

app.layout = html.Div([
    html.H1("Dice simulator"),

    html.Div([
        html.Label("Select rolls"),
        dcc.Dropdown(id="dropdown", options=dropdown_options, value=10)
    ]),

    html.Button("Roll Dice", id="roll-button", n_clicks=0),
    dcc.Graph(id="dice-result")
])


@app.callback(
    Output("dice-result", "figure"),
    [Input("roll-button", "n_clicks"),
     Input("dropdown", "value")]
)
def roll_dice(n_clicks, num_rolls):
    if n_clicks > 0:
        dice_rolls = [random.randint(1, 6) for _ in range(num_rolls)]
        fig = px.histogram(dice_rolls, nbins=6, title=f"Rolls ({num_rolls} rolls)")
        fig.update_layout(xaxis_title="Roll", yaxis_title="Count")
        return fig
    else:
        return {}


if __name__ == '__main__':
    app.run_server(debug=True)
    app.run_server(host="0.0.0.0", debug=True, port=8050)