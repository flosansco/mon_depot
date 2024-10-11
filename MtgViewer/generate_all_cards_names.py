import json
import os


def get_all_names(json_reference="../JsonRessources/all_cards_10072024.json"):
    json_reference = "../JsonRessources/all_cards_10072024.json"
    print(os.path.isfile(json_reference))


if __name__ == '__main__':
    get_all_names()

