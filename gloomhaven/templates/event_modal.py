import dash_html_components as html
import dash_bootstrap_components as dbc

from ..consts import EVENT_MODAL_BODY_ID, EVENT_MODAL_BUTTON_A_ID, EVENT_MODAL_BUTTON_B_ID, EVENT_MODAL_ID


def render():
    return dbc.Modal(
        [
            dbc.ModalHeader("EVENT"),
            dbc.ModalBody(id=EVENT_MODAL_BODY_ID),

            dbc.ModalFooter([
                dbc.Button("A", id=EVENT_MODAL_BUTTON_A_ID),
                dbc.Button("B", id=EVENT_MODAL_BUTTON_B_ID)
            ],
                className="d-flex justify-content-between"),
        ],
        id=EVENT_MODAL_ID,
        size="md",
        style={"background": "url(road.jpg)"}
        # centered=True,
    )
