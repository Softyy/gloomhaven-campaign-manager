from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import no_update

from ..models.campaign import Campaign
from ..models.scenario import Scenario

from .. import app

from ..consts import MODAL_ID, OPEN_MODAL_ID, CLOSE_MODAL_ID, CYTO_GRAPH_ID, MODAL_BODY_ID, MODAL_HEADER_ID, MODAL_FOOTER_ID, COMPLETE_SCENARIO_ID, FAIL_SCENARIO_ID, STORE_ID, DOWNLOAD_DATA_ID, CLEAR_DATA_ID

from .downloader import dict_to_inline_href
from .odds_and_ends import first_arg_is_greatest


@app.callback(
    [Output(STORE_ID, 'data'),
     Output(DOWNLOAD_DATA_ID, 'href'),
     Output(MODAL_ID, "is_open"),
     Output(MODAL_HEADER_ID, 'children'),
     Output(MODAL_BODY_ID, 'children')],
    [Input(CYTO_GRAPH_ID, 'tapNode'),
     Input(COMPLETE_SCENARIO_ID, "n_clicks_timestamp"),
     Input(FAIL_SCENARIO_ID, "n_clicks_timestamp"),
     Input(CLEAR_DATA_ID, "n_clicks_timestamp"),
     Input(CLOSE_MODAL_ID, "n_clicks_timestamp")],
    [State(STORE_ID, 'data')])
def update_local_storage_and_handle_modal(node, success_click_ts, fail_click_ts, erase_click_ts, close_click_ts, store_data):
    if success_click_ts == fail_click_ts == erase_click_ts == close_click_ts == node == None:
        raise PreventUpdate

    store_data = store_data or {}
    node_data = node['data'] if node else None
    node_ts = node['timeStamp'] if node else -1
    success_click_ts = success_click_ts or -1
    fail_click_ts = fail_click_ts or -1
    erase_click_ts = erase_click_ts or -1
    close_click_ts = close_click_ts or -1

    campaign = Campaign(**store_data)

    if first_arg_is_greatest(success_click_ts, fail_click_ts, erase_click_ts, node_ts, close_click_ts):
        campaign.complete_scenario(int(node_data['id']))
        return campaign.to_dict(), dict_to_inline_href(campaign.to_dict()), False, no_update, no_update

    elif first_arg_is_greatest(fail_click_ts, success_click_ts, erase_click_ts, node_ts, close_click_ts):
        campaign.fail_scenario(int(node_data['id']))
        return campaign.to_dict(), dict_to_inline_href(campaign.to_dict()), False, no_update, no_update

    elif first_arg_is_greatest(erase_click_ts, success_click_ts, fail_click_ts, node_ts, close_click_ts):
        campaign = Campaign()
        return campaign.to_dict(), dict_to_inline_href(campaign.to_dict()), no_update, no_update, no_update

    elif first_arg_is_greatest(node_ts, success_click_ts, fail_click_ts, erase_click_ts, close_click_ts):
        scenario: Scenario = Campaign.get_scenario(int(node_data["id"]))
        return no_update, no_update, True, f'{scenario.id} - {scenario.title}', Campaign.text_to_html(scenario.introduction)

    elif first_arg_is_greatest(close_click_ts, node_ts, success_click_ts, fail_click_ts, erase_click_ts):
        return no_update, no_update, False, no_update, no_update
