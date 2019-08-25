import dash_html_components as html
import dash_bootstrap_components as dbc

from ..consts import TOAST_ACHIEVEMENT_ID, TOAST_NEW_LOCATION_ID


def render():
    return (dbc.Toast(
        "Notifications will go here",
        id=TOAST_ACHIEVEMENT_ID,
        header="Achievements Earned!",
        is_open=False,
        dismissable=True,
        icon="success",
        fade=True,
        # top: 66 positions the toast below the navbar
        style={"position": "fixed", "top": 10, "right": 10, "width": 350},
    ),
        dbc.Toast(
        "Notifications will go here",
        id=TOAST_NEW_LOCATION_ID,
        header="New Locations!",
        is_open=False,
        dismissable=True,
        icon="info",
        fade=True,
        # top: 66 positions the toast below the navbar
        style={"position": "fixed", "top": 66, "right": 10, "width": 350},
    ))
