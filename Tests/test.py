#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint

import requests
import mtgsdk
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

sets = Set.all()

# for set in sets:
#     cards = Card.where(subtypes='human,soldier').where(set=set.code).all()
#     for card in cards:
#         print(card.name)

jirina = Card.find("484715")  # type:Card

print(jirina.name, jirina.type)
print(jirina.cmc)
print(jirina.colors)
print(jirina.multiverse_id)
print(jirina.power, jirina.toughness)
print(jirina.original_text)
print(jirina.mana_cost)

# for foreign_names in jirina.foreign_names:
#     if foreign_names["language"] == "French":
#         pprint.pprint(foreign_names)


# def get_card_id(card_name):
#     # Recherche de la carte par nom
#     cards = Card.where(name=card_name).all()
#
#     # Vérification si une carte a été trouvée
#     if cards:
#         # Affichage de l'ID de la première carte trouvée
#         print(f"L'ID de la carte '{card_name}' est : {cards[0].id}")
#     else:
#         print(f"Aucune carte trouvée avec le nom '{card_name}'.")
#
#
# if __name__ == "__main__":
#     # Remplacez "Nom de la carte" par le nom réel de la carte que vous recherchez
#     card_name_to_search = "Jirina Kudro"
#     get_card_id(card_name_to_search)

"""
Field Marshal
Field Marshal
Honor Guard
Kjeldoran Royal Guard
Loyal Sentry
Benalish Hero
Abzan Falconer
Doomed Traveler
Mentor of the Meek
Militia Bugler
Hero of the Games
Tenth District Legionnaire
Mentor of the Meek
Auriok Salvagers
Crusader of Odric
Fencing Ace
Thraben Inspector
Veteran Explorer
Swiftblade Vindicator
Weapons Trainer
Benalish Hero
Benalish Hero
Benalish Hero
Sicarian Infiltrator
Sicarian Infiltrator
Commissar Severina Raine
Commissar Severina Raine
Company Commander
Company Commander
Bastion Protector
Bastion Protector
Benalish Hero
Pikemen
Benalish Hero
Pikemen
Auriok Salvagers
Benalish Hero
D'Avenant Archer
Icatian Phalanx
Icatian Scout
Kjeldoran Royal Guard
Kjeldoran Skycaptain
Pikemen
Shield Bearer
"""