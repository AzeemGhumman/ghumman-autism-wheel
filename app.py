from dash import Dash, html, dcc, callback, Output, Input, ALL
from generate_figure import generateRadialFigure
import dash_mantine_components as dmc
import dash_split_pane
from helper import generateRows, parseData
from data import getSectors, getMockData


app = Dash(__name__)
app.title = "Autism Wheel"

server = app.server

app.layout = html.Div(
    [
        dmc.Title(f"Autism Wheel", order=1,
                  style={"marginTop": "10px", "textAlign": "center"}),
        html.Br(),
        html.Br(),

        dash_split_pane.DashSplitPane(
            children=[
                html.Div(className="fleft", children=generateRows()), html.Div(className="fright", children=[
                    dmc.Checkbox(id="mock", label="Show mock data",
                                 mb=10, checked=False),
                    dcc.Graph(
                        id="graph-content",
                        config={
                            "modeBarButtonsToRemove": ["zoom", "select", "lasso2d"],
                            "displaylogo": False,
                        },
                    ),
                ],
                    style={'alignItems': 'center'})],
            id="splitter",
            split="vertical",
            size="30%",
            style={"margin": "30px"},
            resizerClassName="Resizer",
            # primary="second"
        )



        # html.Div(className='wrap', children=[
        #     html.Div(className="fleft", children=generateRows()),
        #     html.Div(className="fright", children=[
        #         dmc.Checkbox(id="mock", label="Show mock data",
        #                      mb=10, checked=False),
        #         dcc.Graph(
        #             id="graph-content",
        #             config={
        #                 "modeBarButtonsToRemove": ["zoom", "select", "lasso2d"],
        #                 "displaylogo": False,
        #             },
        #         ),
        #     ]),
        # ])
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
