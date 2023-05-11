import plotly.graph_objects as go
from data import getColors


def annotate(text, x, y, fig):
    fig.add_annotation(
        x=x,
        y=y,
        text=text,
        # font={"family": "sans serif", "size": 20, "color": "LightSeaGreen"},
        font={"size": 20},
        showarrow=False,
    )


def generateRadialFigure(data):
    total_sections = len(data)

    plot_sectors = []
    for sector_idx, item in enumerate(data):
        sector_name, sector_value = item
        if sector_value is None:
            continue
        plot_sectors.append(
            go.Barpolar(
                r=[sector_value],
                theta=[sector_idx * 360 / total_sections],
                width=[360 / total_sections],
                marker_color=getColors()[sector_idx],
                marker_line_color="black",
                marker_line_width=1,
                opacity=0.75,
                showlegend=True,
                hoverinfo="skip",
                name=sector_name,
            )
        )

    plot_boundaries = go.Barpolar(
        r=[1.0] * total_sections,
        theta=[i * 360 / total_sections for i in range(total_sections)],
        width=[360 / total_sections] * total_sections,
        marker_color=["white"] * total_sections,
        marker_line_color="black",
        marker_line_width=3,
        opacity=0.3,
        showlegend=False,
        hoverinfo="skip",
    )

    missing_sectors = [idx for (idx, value) in enumerate(data) if value[1] is None]
    print("Missing Sectors: ", missing_sectors)
    plot_missing_sectors = go.Barpolar(
        r=[1.0] * len(missing_sectors),
        theta=[idx * 360 / total_sections for idx in missing_sectors],
        width=[360 / total_sections] * len(missing_sectors),
        marker_color=["white"] * len(missing_sectors),
        marker_line_color="black",
        marker_line_width=0,
        opacity=1.0,
        showlegend=False,
        hoverinfo="skip",
    )

    figure_data = [plot_missing_sectors] + plot_sectors + [plot_boundaries]

    fig = go.Figure(data=figure_data)

    fig.update_layout(
        template=None,
        polar=dict(
            radialaxis=dict(range=[0, 1], showticklabels=False, ticks=""),
            angularaxis=dict(showticklabels=False, ticks=""),
            radialaxis_showline=False,
            gridshape="circular",
        ),
        dragmode=False,
        autosize=False,
        width=1000,
        height=1000,
        legend_title_text="Categories",
    )

    fig.update_polars(angularaxis_color="#000")
    fig.update_polars(angularaxis_gridcolor="#FFF")

    # annotate("First Category", 0.78, 0.6, fig)
    # annotate("Second Category", 0.3, 1.1, fig)
    # annotate("Third Category", 0.27, 0.0, fig)

    # fig.add_annotation(x=0.8, y=0.6, text="Some category", showarrow=False)
    # fig.add_annotation(x=0.8, y=0.6, text="Some category", showarrow=False)

    return fig
