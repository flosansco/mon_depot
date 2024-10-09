import os.path
import pprint
import sqlite3
import json

import requests
from mtgsdk import Card


# Fonction pour créer la base de données et la table
def creer_base_de_donnees():
    conn = sqlite3.connect('ma_base_de_donnees_0710.db')
    cursor = conn.cursor()

    # Création de la table "cartes"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cartes (
            name TEXT PRIMARY KEY,
            type TEXT,
            mana TEXT
        )
    ''')

    conn.commit()
    conn.close()


def generer_json():
    """
    Fonction test pour générer un json
    :return:
    """
    dico = {}
    cards = Card.all()  # futur contenu de la BDD
    for carte in cards:
        dico[carte.name] = {"type": carte.type, "mana": carte.mana_cost}

    with open("card.json", 'w') as fichier_json:
        json.dump(dico, fichier_json, indent=2)
    # pprint.pprint(dico)


# Fonction pour ajouter des données depuis un fichier JSON
def ajouter_donnees_depuis_json(nom_fichier):
    """
    Charge le fichier json et charge ses données dans une BDD

    :param nom_fichier:
    :return:
    """
    conn = sqlite3.connect('ma_base_de_donnees_0710.db')
    cursor = conn.cursor()

    if os.path.isfile(nom_fichier):

        with open(nom_fichier, 'r', encoding='utf-8') as fichier_json:
            print("Loading json, might take a while ...")
            donnees = json.load(fichier_json)
            print("Json loading finished")

            for dico in donnees:
                try:
                    name = dico["name"]
                    mana_cost = dico["mana_cost"]
                    type_line = dico["type_line"]
                    cursor.execute("INSERT OR IGNORE INTO cartes (name, mana, type) VALUES (?, ?, ?)",
                                   (name, mana_cost, type_line))

                except KeyError:
                    print("{} : Unknown mana or type".format(name))
    else:
        print("File {} does not exists".format(nom_fichier))

    conn.commit()
    conn.close()


def lire_bdd():
    # Chemin de la base de données SQLite
    chemin_base_de_donnees = "ma_base_de_donnees_0710.db"

    # Connexion à la base de données
    conn = sqlite3.connect(chemin_base_de_donnees)
    cursor = conn.cursor()

    # Sélection de toutes les colonnes dans la table 'utilisateurs'
    cursor.execute('SELECT * FROM cartes')

    # Récupération des résultats
    resultats = cursor.fetchall()

    # Affichage des résultats
    for row in resultats:
        print(row)

    # Fermeture de la connexion
    conn.close()


# json_file = input("Taper le nom du fichier json à ajouter dans la BDD : ")
json_file = "../JsonRessources/ALL_CARDS_BDD_10072024.json"
ajouter_donnees_depuis_json(json_file)
