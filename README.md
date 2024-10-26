# Système intelligent de tri des déchets ménagers

## Description
Ce projet vise à développer un système intelligent capable de trier automatiquement les déchets en utilisant un modèle de classification d’image. Le système est équipé d’une caméra et utilise un modèle de machine learning pour identifier et trier les déchets en différentes catégories.

## Fonctionnalités
- Classification d’image : Utilisation d’un modèle de machine learning pour identifier les types de déchets.
- Tri automatique : Les déchets sont triés automatiquement en fonction de leur catégorie (organiques, recyclable et autres).

## Prérequis

- **Python 3.x** : Télecharger et installer Python sur votre machine.
  
- **Bibliothèques nécessaires** : la commande ci-dessous dans le guide d'installation permet d'installer toutes les dépendances nécessaire.
  
- **Microcontrôleur**: une Raspberry pi 3 ou plus serait l'idéal mais un microcontrôleur similaire à la Raspberry pi pourrait fonctionner, il suffit d'essayer pour se faire une idée.
  
- **Caméra**: un module caméra Raspberry V2.1, 8MP est conseillé mais vous pouvez tester les versions ultérieures pour se faire une idée.

## Guide d'installation

la commande ci dessous permet d'installer toutes les dépendances nécessaires pour ce projet :

```bash
pip install -r requirements.txt
```

## Fichiers Principaux

1. **main.py** : Ce fichier est le point d'entrée du programme, il suffit de copier et executer la commande ci-dessous pour lancer le programme :

```bash
python3 main.py
```

2. **manager_image_capture.py** : Ce fichier contient une classe `ImageCaptureSystem`, qui gère la capture des images à l'aide de la caméra Raspberri Pi V2.1, 8MP. Il inclut des fonctions pour capturer une image initiale et une image finale, ainsi qu'une fonction qu'on pourrait surnommer de transitoire `process_images`, elle permet de lancer le début de la comparaison et l'initialisation des paramètres de la fonction `comparer_images`.

3. **image_comparison.py** : Ce fichier définit la fonction `comparer_images`, qui prend en entrée les chemins des deux images capturées. Elle utilise des techniques de traitement d'image pour calculer le score de similarité (SSIM) et le pourcentage de différence entre les images.

4. **analyze_classification.py** : Ce fichier contient une fonction `analyze_image_with_tflite` qui analyse l'image enregistré au niveau de la fonction `comparer_images` dans le cas où les deux images sont différentes, cette fonction reçoit en paramètre l'image à analyser et le chemin du modèle TFlite.


