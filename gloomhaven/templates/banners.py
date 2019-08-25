import dash_html_components as html

from ..consts import BANNERS_ID


def render():
    return html.Div(id=BANNERS_ID, className="banners")
