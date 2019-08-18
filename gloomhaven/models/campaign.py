from ..models.scenario import Scenario

from ..consts import SCENARIOS


class Campaign():

    def __init__(self, available_scenarios: [int] = [1], completed_scenarios: [int] = [], attempted_scenarios: [int] = [], failed_scenarios: [int] = [], global_achievements: [str] = [], party_achievements: [str] = []):
        self.available_scenarios = available_scenarios
        self.completed_scenarios = completed_scenarios
        self.attempted_scenarios = attempted_scenarios
        self.failed_scenarios = failed_scenarios
        self.global_achievements = global_achievements
        self.party_achievements = party_achievements

    @staticmethod
    def get_scenario(id: int) -> Scenario:
        return next(
            s for s in SCENARIOS if s.id == id)

    def complete_scenario(self, scenario_id: int):

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
            self.party_achievements = [
                a for a in self.global_achievements if a not in scenario.lost_achievements]

        # only add new scenarios that haven't already been found.
        new_scenarios = [
            s for s in scenario.new_locations if s not in self.available_scenarios]

        # remove scenario just completed and add the new ones
        self.available_scenarios.remove(scenario_id)
        self.available_scenarios.extend(new_scenarios)

    def fail_scenario(self, scenario_id: int):
        self.attempted_scenarios.append(scenario_id)
        self.failed_scenarios.append(scenario_id)

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
