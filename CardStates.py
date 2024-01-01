from enum import Enum


class CardState(Enum):
    IN_DECK = 1
    IN_HAND = 2
    IN_CIMETERY = 3
    ON_BORD = 4
    EXILED = False
    TAPPED = False
