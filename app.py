from dash import Dash, html, dcc, callback, Output, Input, ALL
from generate_figure import generateRadialFigure
import dash_mantine_components as dmc
from helper import generateRows, parseData
from data import getSectors, getMockData

app = Dash(__name__)

server = app.server

app.layout = html.Div(
    [
        dmc.Title(f"Ghumman's Autism Wheel", order=1, style={"margin-top": "10px"}),
        html.Br(),
        html.Br(),
        html.Div(generateRows()),
        dmc.Checkbox(id="mock", label="Show mock data", mb=10, checked=False),
        dcc.Graph(
            id="graph-content",
            config={
                "modeBarButtonsToRemove": ["zoom", "select", "lasso2d"],
                "displaylogo": False,
            },
        ),
    ]
)


@callback(
    Output("graph-content", "figure"),
    Input({"type": "points", "index": ALL}, "value"),
    Input({"type": "total", "index": ALL}, "value"),
    Input("mock", "checked"),
    prevent_initial_callbacks=True,
)
def update_graph(points, total, mock):
    if mock is False:
        items = list(zip(points, total))
        dataset = list(zip(getSectors(), parseData(items)))
        return generateRadialFigure(dataset)
    else:
        return generateRadialFigure(list(zip(getSectors(), getMockData())))


if __name__ == "__main__":
    app.run_server(debug=True)
