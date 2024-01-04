import glob
import json

import requests


def charger_les_suggestions():
    """
    Charge la liste des nom à partir du fichier mis à disposition sur Scryfall : https://scryfall.com/docs/api/bulk-data

    :return:
    """
    names = list()

    with open("all-cards-20240104101309.json", 'r', encoding="utf-8") as all_card_json:
        print("Chargement du fichier json, peut prendre 1 min")
        datas = json.load(all_card_json)
        for data in datas:  # type: dict
            card_name = data.get("name")
            if card_name not in names:
                names.append(card_name)

    print("Dump de tous les noms existants dans un fichier, renvoie une liste")
    with open("all_cards_name.json", "w") as fichier:
        json.dump(names, fichier)


def charger_les_suggestions_http():
    """
    Pareil qu'au dessus mais avec des requetes http, ça me sera surement utile avec le moteur de jeu
    Process par paging

    :return:
    """
    names = list()
    print("Chargement des suggestions ...")
    data = {"next_page": None}

    while True:
        cards_url = "https://api.scryfall.com/cards/search?q=*" \
            if data["next_page"] is None else data["next_page"]
        response = requests.get(cards_url)
        data = response.json()
        # dump TOUTES les données de la responde
        # with open("data.json", 'w') as fichier_json:
        #     json.dump(data, fichier_json, indent=2)

        if "next_page" not in data:
            break

        for d in data.get("data"):
            names.append(d["name"])

    return names


