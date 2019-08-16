import json
from dash.dependencies import Input, Output, State

from .. import app

from ..consts import CYTO_GRAPH_ID, DUMMY_ID

@app.callback(Output(DUMMY_ID, 'children'),
              [Input(CYTO_GRAPH_ID, 'tapNodeData')])
def displayTapNodeData(data):
    print(data)
    return json.dumps(data, indent=2)
