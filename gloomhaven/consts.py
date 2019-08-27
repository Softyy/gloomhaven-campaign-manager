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

OPEN_MODAL_ID = 'open-scenario-modal'
CLOSE_MODAL_ID = 'close-scenario-modal'
MODAL_ID = 'scenario-modal'
MODAL_HEADER_ID = 'scenario-modal-header'
MODAL_BODY_ID = 'scenario-modal-body'
MODAL_FOOTER_ID = 'scenario-modal-footer'

OPEN_CAMPAIGN_MODAL_ID = 'open-campaign-modal'
CLOSE_CAMPAIGN_MODAL_ID = 'close-campaign-modal'
CAMPAIGN_MODAL_ID = 'campaign-modal'
CAMPAIGN_MODAL_HEADER_ID = 'campaign-modal-header'
CAMPAIGN_MODAL_BODY_ID = 'campaign-modal-body'
CAMPAIGN_MODAL_FOOTER_ID = 'campaign-modal-footer'

COMPLETE_SCENARIO_ID = 'scenario-completed'
FAIL_SCENARIO_ID = 'scenario-failed'
TOAST_ACHIEVEMENT_ID = 'toast-achievements'
TOAST_NEW_LOCATION_ID = 'toast-new-locations'

PROSPERITY_ID = 'prosperity-counter'
PARTY_ACHIEVEMENT_LIST_ID = 'party-achievements'

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
        'selector': '.available',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': '#007bff'
        }
    },
    {
        'selector': '.completed',
        'style': {
            'font-family': 'Pirata One',
            'background-color': '#28a745',
        }
    },
    {
        'selector': '.blocked',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': '#dc3545',
        }
    },
    {
        'selector': '.attempted',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'background-color': '#ffc107',
        }
    },
    # This last entry needs to be here for the logic on the hover to work.
    {
        'selector': '.dummy',
        'style': {}
    }
]


# Game database as consts.

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "scenarioPaths.json"), encoding='utf-8') as data_file:
    json_array = json.load(data_file)
    SCENARIOS = [Scenario(**values) for values in json_array]

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "globalAchievements.json"), encoding='utf-8') as data_file:
    json_array = json.load(data_file)
    GLOBAL_ACHIEVEMENTS = [GlobalAchievement(
        **values) for values in json_array]
