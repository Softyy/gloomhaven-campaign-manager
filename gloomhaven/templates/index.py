import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import dash_bootstrap_components as dbc


from ..consts import CYTO_GRAPH_ID, DUMMY_ID, SCENARIOS, SCENARIO_NODE_PARENTS, STORE_ID, CLEAR_DATA_ID, DOWNLOAD_DATA_ID, CYTO_STYLESHEET, OPEN_CAMPAIGN_MODAL_ID, MAP_TOGGLE_ID

from .banners import render as banners
from .scenario import render as scenario_modal
from .toasts import render as toasts
from .campaign_stats import render as campaign_modal
from .event_modal import render as event_modal


def render():
    return html.Div([
        dcc.Store(id=STORE_ID, storage_type='local'),
        scenario_modal(),
        campaign_modal(),
        event_modal(),
        dbc.NavbarSimple([
            daq.BooleanSwitch(id=MAP_TOGGLE_ID,
                              children=html.I(
                                  className="fas fa-map-marked"),
                              className="m-1"),
            dbc.Button(id=OPEN_CAMPAIGN_MODAL_ID,
                       children=html.I(
                           className="fas fa-book-open"), className="m-1", color="info"),
            html.A(id=DOWNLOAD_DATA_ID, children=html.I(
                className="fas fa-cloud-download-alt"), download="gloomhaven-campaign-manager-data.json",
                href="", target="_blank", className="btn btn-success m-1"),
            dbc.Button(id=CLEAR_DATA_ID, children=[html.I(
                className="fas fa-trash-alt")], color="danger", className="m-1"),
        ],
            expand=True,
            brand="GCM",
        ),
        banners(),

        cyto.Cytoscape(
            id=CYTO_GRAPH_ID,
            layout={'name': 'cose', 'roots': '[id = "1"]', 'animate': 'True'},
            style={},
            elements=[],
            minZoom=0.5,
            maxZoom=2,
            stylesheet=CYTO_STYLESHEET
        ),
        html.Div(toasts())
    ])
