from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from ..models.campaign import Campaign

from .. import app

from ..consts import CYTO_GRAPH_ID, DUMMY_ID, STORE_ID, BANNERS_ID


@app.callback(Output(STORE_ID, 'data'),
              [Input(CYTO_GRAPH_ID, 'tapNodeData')],
              [State(STORE_ID, 'data')])
def update_local_storage(node_data, store_data):

    if node_data is None or node_data['type'] != 'blue':
        raise PreventUpdate

    store_data = store_data or {}
    campaign = Campaign(**store_data)
    scenario = campaign.get_scenario(int(node_data['id']))
    campaign.complete_scenario(scenario.id)
    return campaign.to_dict()


@app.callback([Output(CYTO_GRAPH_ID, 'elements'), Output(BANNERS_ID, 'children')],
              [Input(STORE_ID, 'modified_timestamp')],
              [State(STORE_ID, 'data')])
def update_cyto_graph(ts, store_data):
    if ts is None:
        raise PreventUpdate
    store_data = store_data or {}
    campaign = Campaign(**store_data)
    return campaign.to_cyto_graph(), campaign.create_global_banner_imgs()
