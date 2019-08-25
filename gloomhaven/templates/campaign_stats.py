import dash_html_components as html
import dash_bootstrap_components as dbc

from ..consts import BANNERS_ID, CAMPAIGN_MODAL_BODY_ID, CAMPAIGN_MODAL_ID, CAMPAIGN_MODAL_FOOTER_ID, CAMPAIGN_MODAL_HEADER_ID, CLOSE_CAMPAIGN_MODAL_ID, PROSPERITY_ID, PARTY_ACHIEVEMENT_LIST_ID


def render():
    return dbc.Modal(
        [
            dbc.ModalHeader("Campaign Progress", id=CAMPAIGN_MODAL_HEADER_ID),
            dbc.ModalBody([
                html.H6("Prosperity", style={
                    "border-bottom": "1px solid black"}),
                html.Div(
                    0,
                    id=PROSPERITY_ID
                ),
                html.H6("Party Achievements", style={
                    "border-bottom": "1px solid black"}),
                html.Div(
                    id=PARTY_ACHIEVEMENT_LIST_ID
                )
            ],
                id=CAMPAIGN_MODAL_BODY_ID),
            dbc.ModalFooter([
                dbc.Button("Close", id=CLOSE_CAMPAIGN_MODAL_ID, color="info"),
            ],
                className="d-flex justify-content-between",
                id=CAMPAIGN_MODAL_FOOTER_ID
            ),
        ],
        id=CAMPAIGN_MODAL_ID,
        size="lg",
        # centered=True,
    )
