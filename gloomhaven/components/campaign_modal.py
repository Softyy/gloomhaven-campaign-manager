from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import no_update

from ..models.campaign import Campaign
from ..models.scenario import Scenario

from .. import app

from ..consts import CAMPAIGN_MODAL_ID, OPEN_CAMPAIGN_MODAL_ID, CLOSE_CAMPAIGN_MODAL_ID, PARTY_ACHIEVEMENT_LIST_ID, STORE_ID


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
    Output(PARTY_ACHIEVEMENT_LIST_ID, "children"),
    [Input(STORE_ID, "data")]
)
def update_party_achievements_shown(store_data):
    store_data = store_data or {}
    campaign = Campaign(**store_data)
    return campaign.create_html_party_achievements()
