from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import no_update

from ..models.campaign import Campaign
from ..models.scenario import Scenario

from .. import app

from ..consts import CAMPAIGN_MODAL_ID, OPEN_CAMPAIGN_MODAL_ID, CLOSE_CAMPAIGN_MODAL_ID, PARTY_ACHIEVEMENT_LIST_ID, STORE_ID, EVENT_MODAL_ID, OPEN_CITY_EVENT_MODAL, OPEN_ROAD_EVENT_MODAL, STORE_ID, EVENT_MODAL_BODY_ID, EVENT_MODAL_BUTTON_A_ID, EVENT_MODAL_BUTTON_B_ID


@app.callback(
    Output(CAMPAIGN_MODAL_ID, "is_open"),
    [Input(OPEN_CAMPAIGN_MODAL_ID, "n_clicks"),
     Input(CLOSE_CAMPAIGN_MODAL_ID, "n_clicks")],
    [State(CAMPAIGN_MODAL_ID, "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    [Output(EVENT_MODAL_ID, "is_open"), Output(
        EVENT_MODAL_BODY_ID, "children"),
        Output(EVENT_MODAL_BUTTON_A_ID, "children"),
        Output(EVENT_MODAL_BUTTON_B_ID, "children")],
    [Input(OPEN_CITY_EVENT_MODAL, "n_clicks_timestamp"),
     Input(OPEN_ROAD_EVENT_MODAL, "n_clicks_timestamp")],
    [State(EVENT_MODAL_ID, "is_open"),
     State(STORE_ID, "data")],
)
def toggle_event_modal(n1_ts, n2_ts, is_open, store_data):
    if n1_ts == n2_ts == None:
        raise PreventUpdate

    store_data = store_data or {}
    campaign = Campaign(**store_data)

    n1_ts = n1_ts or -1
    n2_ts = n2_ts or -1

    if n1_ts > n2_ts:
        body, option_a, option_b = campaign.city_road_event_body_to_html()
    else:
        body, option_a, option_b = campaign.city_road_event_body_to_html(
            city_event=False)
    return not is_open, body, option_a, option_b


@app.callback(
    Output(PARTY_ACHIEVEMENT_LIST_ID, "children"),
    [Input(STORE_ID, "data")]
)
def update_party_achievements_shown(store_data):
    store_data = store_data or {}
    campaign = Campaign(**store_data)
    return campaign.create_html_party_achievements()
