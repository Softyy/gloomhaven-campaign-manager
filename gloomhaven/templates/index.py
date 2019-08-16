import dash_cytoscape as cyto
import dash_html_components as html


from ..components.cyto_builder import create_cyto_elements_for_scenarios, SCENARIOS

from ..consts import CYTO_GRAPH_ID, DUMMY_ID

CYTO_STYLESHEET = [
    # {
    #     'selector': 'node',
    #     'style': {
    #         #  'font-family': 'Pirata One',
    #         #  'font-size': 12
    #     }
    # },
    # {
    #     'selector': '.triangle',
    #     'style': {
    #         # 'shape': 'triangle'
    #     }
    # },
    {
        'selector': 'edge',
        'style': {
            'curve-style': 'bezier',
            'line-color': 'blue'
        }
    },
]


def render():
    return html.Div([

        cyto.Cytoscape(
            id=CYTO_GRAPH_ID,
            layout={'name': 'breadthfirst', 'roots': '[id = "1"]'},
            style={'width': '100%', 'height': '100%'},
            elements=create_cyto_elements_for_scenarios(SCENARIOS),
            minZoom=0.5,
            maxZoom=2
            # stylesheet=CYTO_STYLESHEET
        ),
        html.Div(id=DUMMY_ID)
    ])
