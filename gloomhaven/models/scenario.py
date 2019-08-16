class Scenario():

    def __init__(self, id, title, requirements=None, anti_requirements=None, party_achievements=None, global_achievements=None, new_locations=None, subset_of_locations=False, conditional_achievements=None, alt_requirements=None):
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

    def __repr__(self):
        return f'{self.id}-{self.title}'
