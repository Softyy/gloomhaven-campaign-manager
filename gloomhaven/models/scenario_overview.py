from dash_html_components import Img, Div, P

from .scenario import Scenario


class ScenarioOverview():
    def __init__(self, scenario: Scenario):
        self.tiles = scenario.tiles

    def to_html(self):
        return [self.map_str_to_html(tile) for tile in self.tiles]

    def map_str_to_html(self, tile_id: str):
        return Img(src=f'./assets/scenario_tiles/{tile_id}.png', style={"max-width": "50%"})
