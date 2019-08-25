import os
import json
from .models.scenario import Scenario
from .models.achievement import GlobalAchievement


CYTO_GRAPH_ID = 'scenario-paths'
DUMMY_ID = 'dummy'
STORE_ID = 'gloomhaven-campaign-manager-storage'
BANNERS_ID = 'banners'
CLEAR_DATA_ID = 'clear-data'
DOWNLOAD_DATA_ID = 'download-data'
UNDO_STEP_ID = 'undo'
OPEN_MODAL_ID = 'open-modal'
CLOSE_MODAL_ID = 'close-modal'
MODAL_ID = 'modal'
MODAL_HEADER_ID = 'modal-header'
MODAL_BODY_ID = 'modal-body'
MODAL_FOOTER_ID = 'modal-footer'
COMPLETE_SCENARIO_ID = 'scenario-completed'
FAIL_SCENARIO_ID = 'scenario-failed'
TOAST_ACHIEVEMENT_ID = 'toast-achievements'
TOAST_NEW_LOCATION_ID = 'toast-new-locations'

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

CYTO_STYLESHEET = [
    {
        'selector': '.blue',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': 'blue'
        }
    },
    {
        'selector': '.green',
        'style': {
            # 'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': 'green',
        }
    },
    {
        'selector': '.red',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': 'red',
        }
    },
    {
        'selector': '.dummy',
        'style': {}
    }
    # {
    #     'selector': '.triangle',
    #     'style': {
    #         # 'shape': 'triangle'
    #     }
    # },
    # {
    #     'selector': 'edge',
    #     'style': {
    #         'curve-style': 'bezier',
    #         'line-color': 'blue'
    #     }
    # },
]


# Game database as consts.

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "scenarioPaths.json")) as data_file:
    json_array = json.load(data_file)
    SCENARIOS = [Scenario(**values) for values in json_array]

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "globalAchievements.json")) as data_file:
    json_array = json.load(data_file)
    GLOBAL_ACHIEVEMENTS = [GlobalAchievement(
        **values) for values in json_array]
