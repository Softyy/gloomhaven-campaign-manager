import os
import json
from .models.scenario import Scenario


CYTO_GRAPH_ID = 'scenario-paths'
DUMMY_ID = 'dummy'
STORE_ID = 'local-storage'

MAIN_QUEST_NODE = {
    'data': {'id': 'main', 'label': 'Main Quests'}
}

PERSONAL_QUEST_NODE = {
    'data': {'id': 'personal', 'label': 'Personal Quests'}
}

RANDOM_QUEST_NODE = {
    'data': {'id': 'random', 'label': 'Random Scenarios'}
}

SEALED_QUEST_NODE = {
    'data': {'id': 'sealed', 'label': 'Sealed'}
}

CITY_QUEST_NODE = {
    'data': {'id': 'city', 'label': 'City Events'}
}

ROAD_QUEST_NODE = {
    'data': {'id': 'road', 'label': 'Road Events'}
}

SCENARIO_NODE_PARENTS = [
    MAIN_QUEST_NODE,
    # PERSONAL_QUEST_NODE,
    # RANDOM_QUEST_NODE,
    # SEALED_QUEST_NODE,
    # CITY_QUEST_NODE,
    # ROAD_QUEST_NODE
]


with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "scenarioPaths.json")) as data_file:
    json_array = json.load(data_file)
    SCENARIOS = [Scenario(**values) for values in json_array]
