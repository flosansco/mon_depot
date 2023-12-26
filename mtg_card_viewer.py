import tkinter as tk
from mtgsdk import Card
from PIL import Image, ImageTk
import requests
from urllib3.exceptions import InsecureRequestWarning


# Désactive les avertissements de certificat SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class MagicCardViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Magic Card Viewer")

        self.card_images = []

        # Crée une entrée pour chaque carte dans la main du joueur
        self.card_entries = []
        for i in range(2):
            label = tk.Label(master, text=f"Carte {i+1}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            entry = tk.Entry(master)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.card_entries.append(entry)

        # Bouton pour afficher les images des cartes
        btn_show_images = tk.Button(master, text="Afficher les images", command=self.show_card_images)
        btn_show_images.grid(row=7, column=0, columnspan=2, pady=10)

    def get_card_id(self, card_name):
        # Recherche de la carte par nom
        cards = Card.where(name=card_name).all()

        # Renvoie l'ID de la première carte trouvée ou None si aucune carte n'est trouvée
        return cards[0].multiverse_id if cards else None

    def load_card_images(self, card_names):
        self.card_images = []
        for card_name in card_names:
            card_id = self.get_card_id(card_name)
            if card_id:
                card_image_url = f"http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid={card_id}&type=card"
                print(card_image_url)
                image = Image.open(requests.get(card_image_url, stream=True, verify=False).raw)
                image = ImageTk.PhotoImage(image)
                self.card_images.append(image)
            else:
                # Ajoute une image de remplacement si la carte n'est pas trouvée
                image = Image.open("placeholder_image.png")  # Remplacez par le chemin de votre image de remplacement
                image = ImageTk.PhotoImage(image)
                self.card_images.append(image)

    def show_card_images(self):
        card_names = [entry.get() for entry in self.card_entries]
        self.load_card_images(card_names)

        # Crée une nouvelle fenêtre pour afficher les images
        image_window = tk.Toplevel(self.master)
        for i, card_image in enumerate(self.card_images):
            label = tk.Label(image_window, image=card_image)
            label.grid(row=i // 4, column=i % 4, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = MagicCardViewer(root)
    root.mainloop()
