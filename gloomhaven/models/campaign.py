from random import randint
from datetime import datetime as dt
from dash_html_components import Img, P, H6, Div

from ..models.scenario import Scenario
from ..models.achievement import GlobalAchievement
from ..models.scenario_overview import ScenarioOverview
from ..models.scenario_event import ScenarioEvent
from ..models.travel_event import TravelEvent

from ..consts import SCENARIOS, GLOBAL_ACHIEVEMENTS, MAP_NODE, CITY_EVENTS, ROAD_EVENTS


class Campaign():

    def __init__(self, available_scenarios: [int] = [1], completed_scenarios: [int] = [], attempted_scenarios: [int] = [], global_achievements: [str] = ["City Rule: Militaristic"], party_achievements: [str] = [], party_reputation: int = 0, city_deck=[x.id for x in CITY_EVENTS], road_deck: [int] = [x.id for x in ROAD_EVENTS], creation_date=dt.today().strftime("%Y-%m-%d")):
        self.available_scenarios = available_scenarios
        self.completed_scenarios = completed_scenarios
        self.attempted_scenarios = attempted_scenarios
        self.global_achievements = global_achievements
        self.party_achievements = party_achievements
        self.creation_date = creation_date
        self.party_reputation = party_reputation
        self.city_deck = city_deck
        self.road_deck = road_deck

    @staticmethod
    def get_scenario(id: int) -> Scenario:
        return next(
            s for s in SCENARIOS if s.id == id)

    @staticmethod
    def get_global_achievement(title: str) -> GlobalAchievement:
        return next(
            s for s in GLOBAL_ACHIEVEMENTS if s.title == title)

    @staticmethod
    def get_city_event(id: int) -> TravelEvent:
        return next(
            s for s in CITY_EVENTS if s.id == id)

    @staticmethod
    def get_road_event(id: int) -> TravelEvent:
        return next(
            s for s in ROAD_EVENTS if s.id == id)

    def complete_scenario(self, scenario_id: int):

        if scenario_id in self.completed_scenarios or not self.scenario_requirements_met(scenario_id):
            return

        self.completed_scenarios.append(scenario_id)
        self.attempted_scenarios.append(scenario_id)

        scenario: Scenario = self.get_scenario(scenario_id)

        # add new party achievements if any
        if scenario.party_achievements:
            self.party_achievements.extend(scenario.party_achievements)

        # add new global achievements if any
        if scenario.global_achievements:
            self.global_achievements.extend(scenario.global_achievements)

        # remove any achievements if any
        if scenario.lost_achievements:
            self.party_achievements = [
                a for a in self.party_achievements if a not in scenario.lost_achievements]
            self.global_achievements = [
                a for a in self.global_achievements if a not in scenario.lost_achievements]

        # only add new scenarios that haven't already been found.
        new_scenarios = [
            s for s in scenario.new_locations if s not in self.available_scenarios + self.completed_scenarios]

        # remove scenario just completed and add the new ones
        self.available_scenarios.remove(scenario_id)
        self.available_scenarios.extend(new_scenarios)

        return scenario

    def fail_scenario(self, scenario_id: int):
        self.attempted_scenarios.append(scenario_id)

    def scenario_requirements_met(self, scenario_id: int) -> bool:
        scenario: Scenario = self.get_scenario(scenario_id)

        requirements_met = True
        achievements = self.party_achievements + self.global_achievements

        for req in scenario.requirements:
            if req not in achievements:
                requirements_met = False

        # Only works due to max of 1 alt req in game.
        for alt_req in scenario.alt_requirements:
            if alt_req in achievements:
                requirements_met = True

        for anti_req in scenario.anti_requirements:
            if anti_req in achievements:
                requirements_met = False

        return requirements_met

    def to_dict(self):
        return self.__dict__

    def to_cyto_graph(self, map_mode_flag=False):
        return self.create_cyto_elements_for_scenarios(map_mode_flag=map_mode_flag)

    def create_scenario_cyto_node(self, scenario: Scenario, className='available'):
        return {
            'data': {'id': scenario.id, 'label': scenario.title, 'parent': scenario.scenario_type, 'type': className,
                     'image_url': self.get_location_image_url(scenario.id)},
            'classes': className
        }

    @staticmethod
    def get_location_image_url(scenario_id):
        if scenario_id in (11, 12):
            scenario_id = '11-12'
        elif scenario_id in (35, 36):
            scenario_id = '35-36'
        return f'/assets/world-map/{scenario_id}.png'

    def create_cyto_edge(self, p1: int, p2: int):
        return {'data': {'source': p1, 'target': p2}, 'style': {
            'mid-source-arrow-fill': 'filled', 'mid-target-arrow-shape': 'vee'},
            'selectable': False}

    def create_cyto_elements_for_scenarios(self, map_mode_flag=False):
        possible_s = [
            s for s in self.available_scenarios if self.scenario_requirements_met(s)]
        impossible_s = [
            s for s in self.available_scenarios if not self.scenario_requirements_met(s)]
        attempted_s = [
            s for s in possible_s if s in self.attempted_scenarios]
        unattempted_s = [
            s for s in possible_s if s not in self.attempted_scenarios]

        s_todo = [self.get_scenario(s) for s in unattempted_s]
        nodes_todo = [self.create_scenario_cyto_node(
            s, 'available') for s in s_todo]

        s_tried = [self.get_scenario(s) for s in attempted_s]
        nodes_tried = [self.create_scenario_cyto_node(
            s, 'attempted') for s in s_tried]

        s_done = [self.get_scenario(s) for s in self.completed_scenarios]
        nodes_done = [self.create_scenario_cyto_node(
            s, 'completed') for s in s_done]
        edges_done = []

        s_blocked = [self.get_scenario(s) for s in impossible_s]
        nodes_blocked = [self.create_scenario_cyto_node(
            s, 'blocked') for s in s_blocked]

        parent_nodes = []

        if map_mode_flag:
            parent_nodes = [MAP_NODE]
        else:
            edges_done = [self.create_cyto_edge(s.id, n)
                          for s in s_done for n in s.new_locations]
        return nodes_todo + nodes_tried + nodes_done + edges_done + nodes_blocked + parent_nodes

    def create_global_banner_imgs(self):
        global_achievements = [
            self.get_global_achievement(t) for t in self.global_achievements]
        return [Img(src=f'{ga.banner}', className="banners") for ga in global_achievements]

    @classmethod
    def undo_last_attempt(cls, campagin):
        campagin.completed_scenarios.pop(-1)
        new_campaign = cls(creation_date=campagin.creation_date)
        for completed_scenario_id in campagin.completed_scenarios:
            new_campaign.complete_scenario(completed_scenario_id)
        return new_campaign

    def __repr__(self):
        return f'available_scenarios: {self.available_scenarios}, completed_scenarios: {self.completed_scenarios}'

    def remove_completed_scenario(self, scenario_id: int):
        scenario = self.get_scenario(scenario_id)
        if scenario_id not in self.completed_scenarios:
            raise Exception(f'Scenario {scenario} hasn\'t been completed')

    def create_toast_achievement_of_unlocks(self, scenario_id: int):
        scenario = self.get_scenario(scenario_id)
        party_section = [
            P("Party", style={"border-bottom": "1px solid black"})]
        party_section += [P(a) for a in scenario.party_achievements]

        global_section = [
            P("Global", style={"border-bottom": "1px solid black"})]
        global_section += [P(a) for a in scenario.global_achievements]

        return party_section if len(party_section) > 1 else [] + global_section if len(global_section) > 1 else []

    def create_html_party_achievements(self):
        return [P(a) for a in self.party_achievements]

    @classmethod
    def create_modal_scenario_text_body(cls, scenario_id: int, show_conclusion=False, show_requirements_not_met=False, progress_marker: int = 0):
        scenario = cls.get_scenario(scenario_id)
        scenario_overview = ScenarioOverview(scenario)

        if show_requirements_not_met:
            requirements_section = cls.create_html_section(
                "Requirements", html_body=scenario.requirements_to_html())
            return requirements_section

        introduction_section = cls.create_html_section(
            "Introduction", scenario.introduction)

        special_rules_section = cls.create_html_section(
            "Special Rules", scenario.special_rules)

        goal_section = cls.create_html_section(
            "Goal", scenario.goal)

        map_section = scenario_overview.to_html()

        midgame_section = []

        if 1 <= progress_marker or (show_conclusion and scenario.event_1.exists()):
            midgame_section = cls.event_to_html(
                midgame_section, 1, scenario.event_1)

        if 2 <= progress_marker or (show_conclusion and scenario.event_2.exists()):
            midgame_section = cls.event_to_html(
                midgame_section, 2, scenario.event_2)

        if 3 <= progress_marker or (show_conclusion and scenario.event_3.exists()):
            midgame_section = cls.event_to_html(
                midgame_section, 3, scenario.event_3)

        conclusion_section = cls.create_html_section(
            "Conclusion", scenario.conclusion)

        return introduction_section + special_rules_section + map_section + goal_section + midgame_section + (conclusion_section if show_conclusion else [])

    @staticmethod
    def text_to_html(text: str):
        return [P(paragraph) for paragraph in text.split('\n')]

    @classmethod
    def event_to_html(cls, midgame_section, number: int, event: ScenarioEvent):
        midgame_section += [Div(
            [H6(number, style={"position": "absolute", "font-size": "x-large", "color": "#861c21", "margin": "5px"}),
             Img(src="./assets/rule.png",
                     className="d-flex", style={"max-width": "400px"})],
            className="d-flex justify-content-center align-items-center")]
        midgame_section += cls.text_to_html(event.text)

        midgame_section += cls.create_html_section(
            'Special Rules', event.special_rules)
        midgame_section += cls.create_html_section(
            'Boss Special 1', event.boss_special_1)
        midgame_section += cls.create_html_section(
            'Boss Special 2', event.boss_special_2)
        return midgame_section

    @classmethod
    def create_html_section(cls, title="Section Title", text="", html_body=None):
        html_to_add = []
        if text != "" or html_body:
            html_to_add += [H6(title,
                               style={"border-bottom": "1px solid black"})]
            html_to_add += html_body if html_body else cls.text_to_html(text)
        return html_to_add

    def city_road_event_body_to_html(self, city_event=True):
        if city_event:
            random_id = randint(0, len(self.city_deck)-1)
            try:
                event_id = self.city_deck[random_id]
            except IndexError:
                print(self.city_deck)
                print(f'city event:{random_id} wasn\'t found, weird')
                return ["Error"]*3
            event = self.get_city_event(event_id)
        else:
            random_id = randint(0, len(self.road_deck)-1)
            try:
                event_id = self.road_deck[random_id]
            except IndexError:
                print(f'road event:{random_id} wasn\'t found, weird')
                return ["Error"]*3
            event = self.get_road_event(event_id)
        return self.text_to_html(event.text), event.option_1, event.option_2
