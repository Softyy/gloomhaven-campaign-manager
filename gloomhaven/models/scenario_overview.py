from dash_html_components import Img, Div, P

from .scenario import Scenario


class ScenarioOverview():
    def __init__(self, scenario: Scenario):
        self.id = scenario.id
        self.tiles = scenario.tiles

    def to_html(self):
        return [Img(src=f'./assets/scenario_layouts/{self.id}.png', className="w-100")]

    def map_str_to_html(self, tile_id: str):
        # Img(src=f'./assets/scenario_tiles/{tile_id}.png', style={"max-width": "50%"})
        return P(tile_id)
