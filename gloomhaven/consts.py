import os
import json
from .models.scenario import Scenario


CYTO_GRAPH_ID = 'scenario-paths'
DUMMY_ID = 'dummy'

with open(os.path.join(os.getcwd(), "gloomhaven",
                       "data", "scenarioPaths.json")) as data_file:
    json_array = json.load(data_file)
    SCENARIOS = [Scenario(**values) for values in json_array]
