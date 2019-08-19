from ..models.scenario import Scenario


def create_scenario_cyto_node(scenario: Scenario):
    return {
        'data': {'id': scenario.id, 'label': scenario.title, 'parent': scenario.scenario_type},
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
