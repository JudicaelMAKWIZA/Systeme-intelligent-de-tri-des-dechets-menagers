from manager_capture_image import ImageCaptureSystem
#from model_inference import send_image_to_model  # Importer la fonction d'envoi

def main():
    system = ImageCaptureSystem()

    while True:
        if not system.capture_initial_image():
            print("Tentative de capture de l'image initiale échouée. Réessayer...")
            continue  # Recommencer le processus

        # Ici, vous pouvez ajouter la logique pour ouvrir la zone de préparation

        if not system.capture_final_image():
            print("Tentative de capture de l'image finale échouée. Réessayer...")
            continue  # Recommencer le processus

        # Comparer les images capturées
        continue_system = system.process_images()
        
        if not continue_system:
            
            print("Le système continue. Envoi de l'image finale au modèle pour analyse...")
            #final_image_path = system.get_final_image_path()  # Récupérer le chemin de la deuxième image
            #result = send_image_to_model(final_image_path)  # Envoyer l'image au modèle
            #print(f"Résultat de l'analyse : {result}")  # Afficher le résultat de l'analyse
            #print("Le système a été arrêté. Veuillez actionner le bouton pour recommencer.")
            #break  # Sortir de la boucle si le système doit s'arrêter
        else:
            print("Le système a été arrêté. Veuillez actionner le bouton pour recommencer.")
            #print("Le système continue. Envoi de l'image finale au modèle pour analyse...")
            break


if __name__ == "__main__":
    main()
