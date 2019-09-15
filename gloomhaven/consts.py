import os
import json

from .models.scenario import Scenario
from .models.achievement import GlobalAchievement
from .models.treasure import Treasure
from .models.travel_event import TravelEvent


CYTO_GRAPH_ID = 'scenario-paths'
DUMMY_ID = 'dummy'
STORE_ID = 'gloomhaven-campaign-manager-storage'
BANNERS_ID = 'banners'
CLEAR_DATA_ID = 'clear-data'
DOWNLOAD_DATA_ID = 'download-data'
UNDO_STEP_ID = 'undo'
MAP_TOGGLE_ID = 'map-mode'

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
PROGRESS_SCENARIO_ID = 'scenario-progression'
FAIL_SCENARIO_ID = 'scenario-failed'
TOAST_ACHIEVEMENT_ID = 'toast-achievements'
TOAST_NEW_LOCATION_ID = 'toast-new-locations'

EVENT_MODAL_ID = 'event-modal'
EVENT_MODAL_BODY_ID = 'event-modal-body'
EVENT_MODAL_BUTTON_A_ID = 'option-A'
EVENT_MODAL_BUTTON_B_ID = 'option-B'

OPEN_CITY_EVENT_MODAL = 'city-event-trigger'
OPEN_ROAD_EVENT_MODAL = 'road-event-trigger'

DEFAULT_PROGRESS_TEXT = 'Open door %s'

PROSPERITY_ID = 'prosperity-counter'
PARTY_ACHIEVEMENT_LIST_ID = 'party-achievements'

MAP_NODE = {
    'data': {'id': 'main', 'image_url': '/assets/world-map/gloomhaven-map.png', 'type': 'background'},
    'classes': 'map'
}

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

BASE_ATTACK_MODIFIER_DECK = ['0']*6 + ['1'] * 5 + \
    ['-1'] * 5 + ['-2']*1 + ['2']*1 + ['2x']*1 + ['X']*1

ATTACK_MODIFIER_ONE_TIME_USE_CARDS = [
    'CURSE'
]

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
            'color': '#000000',
            'background-fit': 'cover',
            'background-image': 'data(image_url)'
        }
    },
    {
        'selector': '.map',
        'style': {
            'background-fit': 'cover',
            'background-image': 'data(image_url)',
            'width': 100,
            'height': 100
        }
    },
    {
        'selector': '.completed',
        'style': {
            'font-family': 'Pirata One',
            'color': '#28a745',
            'background-fit': 'cover',
            'background-image': 'data(image_url)'
        }
    },
    {
        'selector': '.blocked',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'color': '#dc3545',
            'background-fit': 'cover',
            'background-image': 'data(image_url)'
        }
    },
    {
        'selector': '.attempted',
        'style': {
            'content': 'data(label)',
            'font-family': 'Pirata One',
            'color': '#ffc107',
            'background-fit': 'cover',
            'background-image': 'data(image_url)'
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

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "treasures.json"), encoding='utf-8') as data_file:
    json_array = json.load(data_file)
    TREASURES = [Treasure(**values) for values in json_array]

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "eventCards", "city.json"), encoding='utf-8') as data_file:
    json_array = json.load(data_file)
    CITY_EVENTS = [TravelEvent(**values) for values in json_array]

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "eventCards", "road.json"), encoding='utf-8') as data_file:
    json_array = json.load(data_file)
    ROAD_EVENTS = [TravelEvent(**values) for values in json_array]
