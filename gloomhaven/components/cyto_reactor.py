import json
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from ..models.campaign import Campaign

from .. import app

from ..consts import CYTO_GRAPH_ID, DUMMY_ID, STORE_ID


@app.callback(Output(STORE_ID, 'data'),
              [Input(CYTO_GRAPH_ID, 'tapNodeData')],
              [State(STORE_ID, 'data')])
def update_local_storage(node_data, store_data):
    store_data = json.loads(store_data or "{}")

    if node_data is None:
        return store_data
    if node_data['type'] != 'blue':
        raise PreventUpdate()
    campaign = Campaign(**store_data)
    scenario = campaign.get_scenario(int(node_data['id']))
    campaign.complete_scenario(scenario.id)
    return campaign.to_json()

@app.callback(Output(CYTO_GRAPH_ID, 'elements'),
              [Input(STORE_ID, 'data')])
def update_cyto_graph(store_data):
    store_data = json.loads(store_data or "{}")
    campaign = Campaign(**store_data)
    return campaign.to_cyto_graph()
