from Card import MyCard
from CardStates import CardState
from mtgsdk import Card


class Joueur:
    def __init__(self, name):
        self.name = name
        self.life = 40
        self.deck_name = ""
        self.bord = {}

    def ajouter_une_carte_au_bord(self, card_name):
        """

        :param card_name:
        :type card_name: str
        :return:
        """
        card = Card.where(name=card_name).all()[0]  # type:Card
        self.bord[card.name] = card.type
        print("{} joue la carte {}".format(self.name, card.name))
        print("Etat du bord de {} : {}".format(self.name, self.bord))

    def attaquer(self, other_player):
        """

        :param other_player:
        :type other_player: Joueur
        :return:
        """
        print("{} is attacking {}".format(self.name, other_player.name))

    def ajouter_un_marqueur(self, marqueur, carte):
        """
        Le marqueur est un dictionnaire de type {"attaque": 1, "défense": 1} ==> dans cet exemple c'est un marqueur +1/+1

        :param marqueur:
        :type marqueur: dict

        :param carte:
        :type carte: Card

        :return:
        """
        print("{} ajout un marqueur {} sur la carte {}".format(self.name, marqueur, carte))




