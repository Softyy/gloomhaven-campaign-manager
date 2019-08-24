import unittest

from gloomhaven.models.campaign import Campaign


class TestCampaignModel(unittest.TestCase):

    def test_scenario_retrival(self):
        campaign = Campaign()
        s = campaign.get_scenario(1)
        self.assertEqual(s.title, "Black Barrow")

        s = campaign.get_scenario(73)
        self.assertEqual(s.title, "Rockslide Ridge")

        s = campaign.get_scenario(50)
        self.assertEqual(s.id, 50)

    def test_scenario_requirements_check(self):
        campaign = Campaign(party_achievements=[
                            "The Scepter and the Voice"], global_achievements=["The Voice Freed"])
        self.assertEqual(campaign.scenario_requirements_met(42), False)

        campaign = Campaign(party_achievements=[
                            "The Voice's Command", "The Voice's Treasure"])
        self.assertEqual(campaign.scenario_requirements_met(40), True)

        campaign = Campaign(party_achievements=["A Demon's Errand"])
        self.assertEqual(campaign.scenario_requirements_met(22), True)

        campaign = Campaign(party_achievements=["Following Clues"])
        self.assertEqual(campaign.scenario_requirements_met(22), True)
