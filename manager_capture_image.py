import time
from picamera2 import Picamera2
from image_comparison import comparer_images

class ImageCaptureSystem:
    def __init__(self):
        self.camera = Picamera2()
        self.initial_image_path = "initial_image1.jpg"
        self.final_image_path = "final_image1.jpg"

    def capture_initial_image(self):
        """Capture la première image de la zone d'analyse vide."""
        try:
            self.camera.start()
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
            time.sleep(10)  # Attendre que le déchet soit déposé
            self.camera.capture_file(self.final_image_path)
            print("La deuxième image a été capturée et sauvegardée avec succès.")
            return True
        except Exception as e:
            print(f"Erreur lors de la capture de l'image finale : {e}")
            return False

    def process_images(self):
        """Traite les images capturées."""
        print("Début de la comparaison des images...")
        comparer_images(self.initial_image_path, self.final_image_path)
