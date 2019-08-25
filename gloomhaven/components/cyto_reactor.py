from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from ..models.campaign import Campaign

from .. import app

from ..consts import CYTO_GRAPH_ID, DUMMY_ID, STORE_ID, BANNERS_ID, CLEAR_DATA_ID, DOWNLOAD_DATA_ID, UNDO_STEP_ID

from .downloader import dict_to_inline_href


@app.callback([Output(CYTO_GRAPH_ID, 'elements'), Output(BANNERS_ID, 'children')],
              [Input(STORE_ID, 'modified_timestamp')],
              [State(STORE_ID, 'data')])
def update_cyto_graph(ts, store_data):
    if ts is None:
        raise PreventUpdate
    store_data = store_data or {}
    campaign = Campaign(**store_data)
    return campaign.to_cyto_graph(), campaign.create_global_banner_imgs()


@app.callback(Output(CYTO_GRAPH_ID, 'stylesheet'),
              [Input(CYTO_GRAPH_ID, 'mouseoverNodeData')],
              [State(CYTO_GRAPH_ID, 'stylesheet')])
def show_past_scenario_title(node_data, stylesheet):
    if node_data is None or node_data is {} or node_data['type'] == 'available' or node_data['type'] == 'attempted':
        raise PreventUpdate
    last_hovered_element_style = stylesheet.pop(-1)

    style_to_show_text = {
        'selector': f'[id = "{node_data["id"]}"]',
        'style': {
            'content': 'data(label)'
        }
    }
    stylesheet.append(style_to_show_text)
    return stylesheet
