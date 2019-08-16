import os
import json

from ..models.scenario import Scenario

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "scenarioPaths.json")) as data_file:
    json_array = json.load(data_file)
    SCENARIOS = [Scenario(**values) for values in json_array]


def create_scenario_cyto_node(scenario: Scenario):
    return {
        'data': {'id': scenario.id, 'label': scenario.title},
        'classes': 'triangle'
    }


def create_cyto_edge(p1: int, p2: int):
    return {'data': {'source': p1, 'target': p2}, 'style': {
        'mid-source-arrow-fill': 'filled', 'mid-target-arrow-shape': 'vee'},
        'selectable': False}


def create_cyto_elements_for_scenarios(scenarios: [Scenario]):
    nodes = [create_scenario_cyto_node(s) for s in scenarios]
    edges = [create_cyto_edge(s.id, n)
             for s in scenarios for n in s.new_locations]
    return nodes + edges
