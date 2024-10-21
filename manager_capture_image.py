import time
import os
from picamera2 import Picamera2
from image_comparison import comparer_images

class ImageCaptureSystem:
    def __init__(self):
        self.camera = Picamera2()
        self.initial_image_path = "initial_image.jpg"
        self.final_image_path = "final_image.jpg"
        self.similarity_count = 0  # Compteur pour les images identiques

    def capture_initial_image(self):
        """Capture la première image de la zone d'analyse vide."""
        try:
            self.camera.start()
            time.sleep(5)  # Attendre que le système soit completement demarrer et prêt
            time.sleep(2)  # Attendre que la caméra soit prête
            self.camera.capture_file(self.initial_image_path)
            print("La première image a été capturée et sauvegardée avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la capture de l'image initiale : {e}")
            return False

    def capture_final_image(self):
        """Capture la seconde image après l'ouverture de la zone."""
        try:
            print("Allons-y... vous avez 10 secondes") #IL Y UNE FERMETURE DE LA ZONE JUSTE APRES QUE L'UTILISATEUR JETTE LE DECHET CAR IL A 15 SECONDES POUR LE FAIRE
            time.sleep(15)  # Attendre que le déchet soit déposé
            self.camera.capture_file(self.final_image_path)
            print("La deuxième image a été capturée et sauvegardée avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la capture de l'image finale : {e}")
            return False

    def process_images(self):
        """Traite les images capturées."""
        time.sleep(3)
        print("Début de la comparaison des images...")
        score, self.similarity_count, continue_system = comparer_images(self.initial_image_path, self.final_image_path, self.similarity_count)
