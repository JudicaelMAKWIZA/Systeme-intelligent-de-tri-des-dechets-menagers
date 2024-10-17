'''
from image_capture_system import ImageCaptureSystem

if __name__ == "__main__":
    servo_pin = 17  # Remplacez par le numéro de votre pin GPIO
    system = ImageCaptureSystem(servo_pin)

    while True:
        if not system.capture_initial_image():
            print("Tentative de capture de l'image initiale échouée. Réessayer...")
            continue  # Recommencer le processus

        system.open_preparation_area()

        if not system.capture_final_image():
            print("Tentative de capture de l'image finale échouée. Réessayer...")
            continue  # Recommencer le processus

        if not system.process_images():
            break  # Sortir de la boucle si le système doit s'arrêter
'''
from manager_capture_image import ImageCaptureSystem
if __name__ == "__main__":
    system = ImageCaptureSystem()

    while True:
        if not system.capture_initial_image():
            print("Tentative de capture de l'image initiale échouée. Réessayer...")
            continue  # Recommencer le processus

        # Ici, vous pouvez ajouter la logique pour ouvrir la zone de préparation si nécessaire

        if not system.capture_final_image():
            print("Tentative de capture de l'image finale échouée. Réessayer...")
            continue  # Recommencer le processus

        # Comparer les images capturées
        system.process_images()
        break  # Sortir de la boucle après la comparaison
