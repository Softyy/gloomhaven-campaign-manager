from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import no_update

from ..models.campaign import Campaign

from .. import app

from ..consts import MODAL_ID, OPEN_MODAL_ID, CLOSE_MODAL_ID, CYTO_GRAPH_ID, MODAL_BODY_ID, MODAL_HEADER_ID, MODAL_FOOTER_ID


@app.callback(
    [Output(MODAL_ID, "is_open"),
     Output(MODAL_HEADER_ID, 'children'),
     Output(MODAL_BODY_ID, 'children')],
    [Input(CYTO_GRAPH_ID, 'tapNode'), Input(CLOSE_MODAL_ID, "n_clicks")],
    [State(MODAL_ID, "is_open")],
)
def toggle_modal(node, close_clicks, is_open):
    node_data = node['data'] if node else None
    if node_data or close_clicks:
        return not is_open, f'{node_data["id"]} {node_data["label"]}', 'THIS IS THE BODY'
    return is_open, "", ""
