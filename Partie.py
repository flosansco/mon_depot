from Joueur import Joueur
from Card import MyCard


class Partie:
    def __init__(self):

        self.nombre_joueurs = 0
        self.current_player = Joueur("Nobody")
        self.joueurs = []
        self.players = []
        self.tour = 1

    def start_tour(self, first_player):
        """

        :param first_player:
        :type first_player: Joueur
        :return:
        """
        print(" =========== Starting tour with {} players =========== ".format(self.nombre_joueurs))
        print("{} are playing".format(self.joueurs))
        self.current_player = first_player
        print("{} commence".format(first_player.name))
        self.selectionner_ordre_de_passage(self.joueurs)

    def selectionner_ordre_de_passage(self, liste_ordre):
        # TODO
        liste_joueur_dans_lordre = self.joueurs
        return liste_joueur_dans_lordre

    def tour_suivant(self):
        self.current_player = self.joueurs[self.tour]
        self.tour = (self.tour + 1) % len(self.joueurs)
        print("Au tour de {}".format(self.current_player))
        return self.current_player

    def ajouter_un_joueur(self, joueur):
        """

        :param joueur:
        :type joueur : Joueur
        :return:
        """
        self.joueurs.append(joueur.name)
        self.players.append(joueur)
        self.nombre_joueurs += 1

    @staticmethod
    def afficher_bord(joueur):
        """

        :param joueur:
        :type joueur: Joueur

        :return:
        """
        print("Bord de {}: {}".format(joueur.name, joueur.bord))


if __name__ == '__main__':

    partie1 = Partie()
    joueur1 = Joueur("Floriane")
    joueur2 = Joueur("Florent")
    joueur3 = Joueur("Goul")

    partie1.ajouter_un_joueur(joueur1)
    partie1.ajouter_un_joueur(joueur2)
    partie1.ajouter_un_joueur(joueur3)

    partie1.start_tour(joueur1)

    joueur1.ajouter_une_carte_au_bord("Jirina")
    joueur1.attaquer(joueur2)

    partie1.tour_suivant()
    joueur2.ajouter_une_carte_au_bord("Sol Ring")
    partie1.afficher_bord(joueur1)

    partie1.tour_suivant()
    partie1.tour_suivant()

