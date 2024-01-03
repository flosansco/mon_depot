from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
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

    def show_card_info(self):
        """
        Display the card searched from the search bare

        :return:
        """
        card_name = self.card_entry.text()

        try:
            # Rechercher la carte par nom
            card = Card.where(name=card_name).all()[0]

            # Afficher les informations de la carte
            info_text = (f"Nom: {card.name}\n"
                         f"Type: {card.type}\n"
                         f"Rareté: {card.rarity}\n"
                         f"Cout de mana: {card.mana_cost}\n"
                         f"Texte: {card.text}")
            self.result_label.setText(info_text)

            # Charger et afficher l'image de la carte
            image_url = card.image_url
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(image_url, stream=True, verify=False).content)
            self.image_label.setPixmap(pixmap)
        except IndexError:
            self.result_label.setText(f"Carte introuvable : {card_name}")
            self.image_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MagicCardViewer()
    viewer.show()
    sys.exit(app.exec_())
