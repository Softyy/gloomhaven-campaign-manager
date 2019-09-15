class TravelEvent():
    def __init__(self, id=0, text: str = "", option_1: str = "", option_2: str = "", default_outcome_1: str = "", default_outcome_1_rewards: str = "", default_outcome_1_cycle: bool = True, pay_outcome_1: str = "", pay_outcome_1_cost: str = "", pay_outcome_1_cycle: bool = True, pay_outcome_1_rewards: [str] = [], default_outcome_2: str = "", default_outcome_2_rewards: [str] = [], default_outcome_2_cycle: bool = True, class_outcome_1: str = "", class_outcome_1_requirements: [str] = [], class_outcome_1_rewards: [str] = [], class_outcome_1_cycle: bool = True):
        self.id = id
        self.text = text
        self.option_1 = option_1
        self.option_2 = option_2
        self.default_outcome_1 = default_outcome_1
        self.default_outcome_2 = default_outcome_2
        self.default_outcome_1_rewards = default_outcome_1_rewards
        self.default_outcome_2_rewards = default_outcome_2_rewards
        self.default_outcome_1_cycle = default_outcome_1_cycle
        self.default_outcome_2_cycle = default_outcome_2_cycle

        self.pay_outcome_1_cost = pay_outcome_1_cost
        self.pay_outcome_1 = pay_outcome_1
        self.pay_outcome_1_cycle = pay_outcome_1_cycle
        self.pay_outcome_1_rewards = pay_outcome_1_rewards
