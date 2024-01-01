from CardStates import CardState
import mtgsdk
from mtgsdk import Card


class MyCard(Card):
    def __init__(self, name):
        super().__init__()
        self.state = CardState.IN_DECK
        self.card_name = name

