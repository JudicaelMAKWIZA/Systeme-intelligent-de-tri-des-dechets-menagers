import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def comparer_images(image1_path, image2_path, seuil_similarite=0.9):
    # Charger les deux images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Vérifier que les images ont été correctement chargées
    if image1 is None or image2 is None:
        print("Erreur lors du chargement des images. Vérifiez les chemins.")
        return

    # Convertir les images en niveaux de gris
    gris1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou Gaussien pour éliminer les petits détails
    flou1 = cv2.GaussianBlur(gris1, (5, 5), 0)
    flou2 = cv2.GaussianBlur(gris2, (5, 5), 0)

    # Calculer l'indice de similarité structurelle (SSIM)
    score, diff = ssim(flou1, flou2, full=True)
    diff = (diff * 255).astype("uint8")  # Conversion en image d'échelle de gris

    # Binariser l'image de différence pour mieux visualiser les variations
    _, diff_binaire = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Calculer le pourcentage de différence (seuils ajustables selon les besoins)
    pourcentage_diff = np.sum(diff_binaire > 0) / diff_binaire.size * 100

    # Afficher le score et le pourcentage de différence
    print(f"Score de similarité (SSIM): {score:.4f}")
    print(f"Pourcentage de différence: {pourcentage_diff:.2f}%")

    # Afficher les résultats de comparaison
    if score >= seuil_similarite:
        print("Les images sont similaires.")
    else:
        print("Les images sont différentes.")
