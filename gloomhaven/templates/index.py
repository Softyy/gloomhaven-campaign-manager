import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


from ..consts import CYTO_GRAPH_ID, DUMMY_ID, SCENARIOS, SCENARIO_NODE_PARENTS, STORE_ID, CLEAR_DATA_ID, DOWNLOAD_DATA_ID, UNDO_STEP_ID, CYTO_STYLESHEET, TOAST_ACHIEVEMENT_ID

from .banners import render as banners
from .scenario import render as scenario_modal


def render():
    return html.Div([
        dcc.Store(id=STORE_ID, storage_type='local'),
        scenario_modal(),
        banners(),
        cyto.Cytoscape(
            id=CYTO_GRAPH_ID,
            layout={'name': 'cose', 'roots': '[id = "1"]', 'animate': 'True'},
            style={'width': '100%', 'height': '600px'},
            elements=[],
            minZoom=0.5,
            maxZoom=2,
            stylesheet=CYTO_STYLESHEET
        ),
        html.Button(id=UNDO_STEP_ID, children="UNDO LAST ACTION"),
        html.Button(id=CLEAR_DATA_ID, children="CLEAR DATA"),
        html.A(id=DOWNLOAD_DATA_ID, children="DOWNLOAD DATA", download="gloomhaven-campaign-manager-data.json",
               href="", target="_blank"),
        dbc.Toast(
            "Notifications will go here",
            id=TOAST_ACHIEVEMENT_ID,
            header="Achievements Earned!",
            is_open=False,
            dismissable=True,
            icon="success",
            fade=True,
            # top: 66 positions the toast below the navbar
            style={"position": "fixed", "top": 66, "right": 10, "width": 350},
        )

    ])
