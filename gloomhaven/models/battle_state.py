import random

from dash_html_components import Img
from ..consts import BASE_ATTACK_MODIFIER_DECK, ATTACK_MODIFIER_ONE_TIME_USE_CARDS


class BattleState():
    def __init__(self, monsters_in_play=[], attack_modifier_deck=BASE_ATTACK_MODIFIER_DECK, attack_modifier_discard=[]):

        self.monsters_in_play = monsters_in_play
        self.attack_modifier_deck = attack_modifier_deck
        self.attack_modifier_discard = attack_modifier_discard

    def shuffle_attack_modifier_deck(self):
        random.shuffle(self.attack_modifier_deck)

    def add_curse_to_attack_modifier_deck(self):
        self.attack_modifier_deck.append("CURSE")
        self.shuffle_attack_modifier_deck()

    def draw_attack_modifier_card(self):
        card = self.attack_modifier_deck.pop()
        self.attack_modifier_discard.append(card)
        return card

    def shuffle_discard_into_deck(self):
        non_removable_discarded_cards = [
            c for c in self.attack_modifier_discard if c not in ATTACK_MODIFIER_ONE_TIME_USE_CARDS]
        self.attack_modifier_deck.extend(non_removable_discarded_cards)
        self.attack_modifier_discard = []
        self.shuffle_attack_modifier_deck()

    def draw_monster_ability_card(self):
        pass

    def modifier_card_to_html(self, card: str):
        return Img(src=f'./assets/attack-modifiers/monster/{card}.png')
