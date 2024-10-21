import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

def comparer_images(image1_path, image2_path, similarity_count):
    # Charger les deux images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Vérifier que les images ont été correctement chargées
    if image1 is None or image2 is None:
        print("Erreur lors du chargement des images. Vérifiez les chemins.")
        return 0, similarity_count, True  # Continuer le système

    # Convertir les images en niveaux de gris
    gris1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou Gaussien pour éliminer les petits détails
    flou1 = cv2.GaussianBlur(gris1, (5, 5), 0)
    flou2 = cv2.GaussianBlur(gris2, (5, 5), 0)

    # Calculer l'indice de similarité structurelle (SSIM)
    score, _ = ssim(flou1, flou2, full=True)

    # Binarisation de l'image de différence
    difference = cv2.absdiff(gris1, gris2)
    _, binarized_diff = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

    # Calculer le pourcentage de différence
    total_pixels = binarized_diff.size
    different_pixels = np.count_nonzero(binarized_diff)
    percentage_difference = (different_pixels / total_pixels) * 100

    # Logique de comparaison
    if score >= 0.9:  # Seuil de similarité
        print("Les images sont identiques.")
        print(f"Pourcentage de différence : {percentage_difference:.2f}%")
        os.remove(image1_path)  # Supprimer la première image
        os.remove(image2_path)  # Supprimer la deuxième image
        return score, similarity_count, False  # Arrêter le système
    else:
        print("Les images sont différentes.")
        print(f"Pourcentage de différence : {percentage_difference:.2f}%")
        similarity_count = 0  # Réinitialiser le compteur
        os.remove(image1_path)  # Supprimer la première image
        os.rename(image2_path, image1_path)  # Renommer la deuxième image
        return score, similarity_count, True  # Continuer le système
