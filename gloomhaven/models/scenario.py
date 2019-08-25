class Scenario():

    def __init__(self, id, title, requirements=[], anti_requirements=[], party_achievements=[], global_achievements=[], new_locations=[], subset_of_locations=False, conditional_achievements=None, alt_requirements=[], lost_achievements=[], personal_requirements=None, scenario_type: str = 'main', introduction: str = "", treasures: [int] = []):
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

    def __repr__(self):
        return f'{self.id}-{self.title}'
