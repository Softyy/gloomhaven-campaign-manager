from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from .. import app

from ..consts import STORE_ID

# output the stored clicks in the table cell.


@app.callback(Output(STORE_ID, 'data'),
              [Input(STORE_ID, 'modified_timestamp')],
              [State(STORE_ID, 'data')])
def update_local_storage(ts, data):
    if ts is None:
        raise PreventUpdate

    data = data or {}

    return data.get('clicks', 0)
