import dash_mantine_components as dmc
from data import getSectors


def generateRows():
    rows = []
    for row_idx, sector in enumerate(getSectors()):
        rows.append(
            dmc.Grid(
                children=[
                    dmc.Col(
                        dmc.Text(
                            sector,
                            size="xl",
                            style={
                                "text-align": "center",
                            },
                        ),
                        span=4,
                        style={
                            "display": "flex",
                            "align-items": "center",
                        },
                    ),
                    dmc.Col(
                        dmc.TextInput(
                            id={"type": "points", "index": row_idx},
                            label="Points",
                            placeholder="",
                            style={"width": 80},
                        ),
                        span=2,
                    ),
                    dmc.Col(
                        dmc.TextInput(
                            id={"type": "total", "index": row_idx},
                            label="Total",
                            placeholder="",
                            style={"width": 80},
                        ),
                        span=2,
                    ),
                ],
                gutter="xl",
            )
        )
    return rows


def parseData(items):
    data = [None] * len(items)
    for idx, item in enumerate(items):
        score, total = item
        try:
            data[idx] = float(score) / float(total)
        except:
            pass
    return data
