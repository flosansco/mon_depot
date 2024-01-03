from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

from mtgsdk import Card
import requests
from urllib3.exceptions import InsecureRequestWarning


# Désactive les avertissements de certificat SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class MagicCardViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Magic Card Viewer')

        # Widgets
        self.label = QLabel('Nom de la carte:', self)
        self.card_entry = QLineEdit(self)
        self.result_label = QLabel(self)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.search_button = QPushButton('Rechercher la carte', self)
        self.search_button.clicked.connect(self.show_card_info)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.card_entry)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Test
        self.card_entry.setText("Jirina Kudro")

    def show_card_info(self):
        """
        Display the card searched from the search bare

        :return:
        """
        card_name = self.card_entry.text()
        self.card_entry.setText("Jirina Kudro")

        try:
            # Rechercher la carte par nom
            # card = Card.where(name=card_name).all()[0]

            scryfall_api_url = f"https://api.scryfall.com/cards/named?exact={card_name}"
            response = requests.get(scryfall_api_url)
            card = response.json()  # type: dict
            # pprint.pprint(card)

            # Afficher les informations de la carte
            info_text = (f"Nom: {card.get("name")}\n"
                         f"Type: {card.get("type_line")}\n"
                         f"Rareté: {card.get("rarity")}\n"
                         f"Cout de mana: {card.get("mana_cost")}\n"
                         f"Texte: {card.get("text")}")
            self.result_label.setText(info_text)

            # Charger et afficher l'image de la carte
            image_url = card.get("image_uris").get("normal")
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(image_url, stream=True, verify=False).content)
            self.image_label.setPixmap(pixmap)
        except Exception as e:
            self.result_label.setText(f"Carte introuvable : {card_name}, error : {e}")
            self.image_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MagicCardViewer()
    viewer.show()
    sys.exit(app.exec_())
