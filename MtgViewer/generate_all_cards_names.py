import ijson
import json
import os
import logging
from LogManager.log_manager import CustomFormatter

# Set up the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Apply the custom formatter to the handler
ch.setFormatter(CustomFormatter())

# Add the handler to the logger
logger.addHandler(ch)


def get_all_names(json_reference="../JsonRessources/all_cards_10072024.json"):
    json_reference = "../JsonRessources/all_cards_10072024.json"
    all_cards_names_list = list()
    json_all_cards_names = "../JsonRessources/all_cards_names.json"

    if os.path.exists(json_all_cards_names) and os.stat(json_all_cards_names).st_size != 0:
        logger.warning(f"Le fichier {json_all_cards_names} existe et contient des données, son contenu sera remplacé.")

    if os.path.isfile(json_reference):
        with open(json_reference, 'r', encoding='utf-8') as fichier_json_ref:
            logger.info("Loading reference infos")
            donnees = ijson.items(fichier_json_ref, 'item')
            for dico in donnees:
                try:
                    name = dico["name"]
                    if name not in all_cards_names_list:
                        all_cards_names_list.append(name)

                except KeyError:
                    logger.error("Key error for {}".format(dico))

            logger.info("Dumping new values")
            with open(json_all_cards_names, 'w', encoding='utf-8') as fichier_json_names:
                json.dump(all_cards_names_list, fichier_json_names, indent=4)


if __name__ == '__main__':
    get_all_names()
