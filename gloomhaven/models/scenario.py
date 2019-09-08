from dash_html_components import P

from .scenario_event import ScenarioEvent


class Scenario():

    def __init__(self, id, title, requirements=[], anti_requirements=[], party_achievements=[], global_achievements=[], new_locations=[], subset_of_locations=False, conditional_achievements=None, alt_requirements=[], lost_achievements=[], personal_requirements=None, scenario_type: str = 'main', introduction: str = "", treasures: [int] = [], conclusion: str = "", goal: str = "Kill all enemies", board_square: str = "A-1", tiles: [str] = ["A1a", "A2b"], event_1: ScenarioEvent = {}, rewards: [str] = [], special_rules: str = "", event_2: ScenarioEvent = {}, event_3: ScenarioEvent = {}, boss_special_1: str = "", boss_special_2: str = ""):
        self.id = id
        self.title = title
        self.requirements = requirements
        self.anti_requirements = anti_requirements
        self.party_achievements = party_achievements
        self.global_achievements = global_achievements
        self.new_locations = new_locations
        self.subset_of_locations = subset_of_locations
        self.conditional_achievements = conditional_achievements
        self.alt_requirements = alt_requirements
        self.lost_achievements = lost_achievements
        self.personal_requirements = personal_requirements
        self.scenario_type = scenario_type
        self.introduction = introduction
        self.treasures = treasures
        self.conclusion = conclusion
        self.goal = goal
        self.tiles = tiles
        self.board_square = board_square
        self.event_1 = ScenarioEvent(**event_1)
        self.event_2 = ScenarioEvent(**event_2)
        self.event_3 = ScenarioEvent(**event_3)
        self.rewards = rewards
        self.special_rules = special_rules
        self.boss_special_1 = boss_special_1
        self.boss_special_2 = boss_special_2

    def requirements_to_html(self):
        requirements = self.text_and_cond_to_html(
            self.requirements, "Complete")
        anti_requirements = self.text_and_cond_to_html(
            self.anti_requirements, "Incomplete")
        alt_requirements = self.text_and_cond_to_html(
            self.alt_requirements, "Complete")
        return requirements + anti_requirements + ([P("Or")] + alt_requirements if len(alt_requirements) > 0 else [])

    @staticmethod
    def text_and_cond_to_html(requirements: str, cond: str):
        return [P(f'{requirement} ({cond})') for requirement in requirements]

    def __repr__(self):
        return f'{self.id}-{self.title}'
