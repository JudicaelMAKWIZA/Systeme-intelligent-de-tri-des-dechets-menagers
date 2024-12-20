from manager_capture_image import ImageCaptureSystem
from analyze_classification import analyze_image_with_tflite  

def main():
    system = ImageCaptureSystem()
    model_path = '/home/judicael/Systeme-intelligent-de-tri-des-dechets-menagers/my_model/classification_dechets_ameliore_v2.tflite'
    image_to_analyze = system.final_image_path

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
            analyze_image_with_tflite(image_to_analyze, model_path)
            break  # Sortir de la boucle 
            #print("Finish...")
        else:
            print("Le système a été arrêté. Veuillez actionner le bouton pour recommencer.")
            #print("Le système continue. Envoi de l'image finale au modèle pour analyse...")
            break


if __name__ == "__main__":
    main()
