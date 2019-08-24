import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from ..consts import CYTO_GRAPH_ID, DUMMY_ID, SCENARIOS, SCENARIO_NODE_PARENTS, STORE_ID, CLEAR_DATA_ID, DOWNLOAD_DATA_ID, UNDO_STEP_ID, MODAL_ID, CLOSE_MODAL_ID, MODAL_BODY_ID, MODAL_HEADER_ID, MODAL_FOOTER_ID

from .banners import render as banners

CYTO_STYLESHEET = [
    {
        'selector': '.blue',
        'style': {
            'content': 'data(label)',
            'background-color': 'blue',
        }
    },
    {
        'selector': '.green',
        'style': {
            # 'content': 'data(label)',
            'background-color': 'green',
        }
    },
    {
        'selector': '.red',
        'style': {
            'content': 'data(label)',
            'background-color': 'red',
        }
    },
    {
        'selector': '.dummy',
        'style': {}
    }
    # {
    #     'selector': '.triangle',
    #     'style': {
    #         # 'shape': 'triangle'
    #     }
    # },
    # {
    #     'selector': 'edge',
    #     'style': {
    #         'curve-style': 'bezier',
    #         'line-color': 'blue'
    #     }
    # },
]


def render():
    return html.Div([
        dcc.Store(id=STORE_ID, storage_type='local'),
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
        dbc.Modal(
            [
                dbc.ModalHeader("Header", id=MODAL_HEADER_ID),
                dbc.ModalBody("This is the content of the modal",
                              id=MODAL_BODY_ID),
                dbc.ModalFooter(
                    dbc.Button("Close", id=CLOSE_MODAL_ID,
                               className="ml-auto"),
                    id=MODAL_FOOTER_ID
                ),
            ],
            id=MODAL_ID,
            size="lg",
            centered=True,
        ),
    ])
