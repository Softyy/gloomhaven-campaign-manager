import json
from urllib import parse

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import no_update

from ..models.campaign import Campaign

from .. import app

from ..consts import CYTO_GRAPH_ID, DUMMY_ID, STORE_ID, BANNERS_ID, CLEAR_DATA_ID, DOWNLOAD_DATA_ID, UNDO_STEP_ID

from .downloader import dict_to_inline_href


@app.callback([Output(STORE_ID, 'data'),
               Output(DOWNLOAD_DATA_ID, 'href')],
              [Input(CYTO_GRAPH_ID, 'tapNode'),
               Input(CLEAR_DATA_ID, 'n_clicks'),
               Input(UNDO_STEP_ID, 'n_clicks')],
              [State(STORE_ID, 'data'),
               State(CLEAR_DATA_ID, 'n_clicks_timestamp'),
               State(UNDO_STEP_ID, 'n_clicks_timestamp')])
def update_local_storage(node, reset_click, undo_click, store_data, reset_click_ts, undo_click_ts):
    node_data = node['data'] if node else None
    node_ts = node['timeStamp'] if node else -1
    store_data = store_data or {}

    # Reset the data to the base constructor of campaign
    if reset_click is not None and reset_click_ts > node_ts:
        campaign = Campaign()
    elif node_data is None or node_data['type'] != 'blue':
        return no_update, dict_to_inline_href(store_data)
    # User wants to undo the last action.
    elif undo_click is not None and undo_click_ts > node_ts:
        campaign = Campaign(**store_data)
        campaign = Campaign.undo_last_attempt(campaign)
    # User wants to progress the campaign
    else:
        campaign = Campaign(**store_data)
        scenario = campaign.get_scenario(int(node_data['id']))
        campaign.complete_scenario(scenario.id)
    return campaign.to_dict(), dict_to_inline_href(campaign.to_dict())


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
    if node_data is None or node_data is {} or node_data['type'] == 'blue':
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
