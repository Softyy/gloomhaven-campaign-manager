import dash_html_components as html
import dash_bootstrap_components as dbc

from ..consts import BANNERS_ID, MODAL_ID, CLOSE_MODAL_ID, MODAL_BODY_ID, MODAL_HEADER_ID, MODAL_FOOTER_ID, COMPLETE_SCENARIO_ID, FAIL_SCENARIO_ID, PROGRESS_SCENARIO_ID, DEFAULT_PROGRESS_TEXT, OPEN_CITY_EVENT_MODAL, OPEN_ROAD_EVENT_MODAL


def render():
    return dbc.Modal(
        [
            dbc.ModalHeader([
                html.H4("Deader", id=MODAL_HEADER_ID),
                dbc.Button("CITY", id=OPEN_CITY_EVENT_MODAL),
                dbc.Button("ROAD", id=OPEN_ROAD_EVENT_MODAL)
            ]),
            dbc.ModalBody("This is the content of the modal",
                          id=MODAL_BODY_ID),
            dbc.ModalFooter([
                dbc.Button("Close", id=CLOSE_MODAL_ID, color="info"),
                html.Div([
                    dbc.Button("Fail",
                               id=FAIL_SCENARIO_ID, color="danger"),
                    dbc.Button(DEFAULT_PROGRESS_TEXT % 1, id=PROGRESS_SCENARIO_ID,
                               color="secondary"),
                    dbc.Button("Complete",
                               id=COMPLETE_SCENARIO_ID, color="success")
                ])],
                className="d-flex justify-content-between",
                id=MODAL_FOOTER_ID
            ),
        ],
        id=MODAL_ID,
        size="lg",
        # centered=True,
    )
