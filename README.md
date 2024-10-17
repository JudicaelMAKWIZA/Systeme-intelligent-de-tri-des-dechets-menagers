# Système intelligent de tri des déchets ménagers

## Description
Ce projet vise à développer un système intelligent capable de trier automatiquement les déchets en utilisant un modèle de classification d’image. Le système est équipé d’une caméra et utilise un modèle de machine learning pour identifier et trier les déchets en différentes catégories.

## Fonctionnalités
- Classification d’image : Utilisation d’un modèle de machine learning pour identifier les types de déchets.
- Tri automatique : Les déchets sont triés automatiquement en fonction de leur catégorie (organiques, recyclable et autres).

## Prérequis

- **Python 3.x** : Télecharger et installer Python sur votre machine.
- **Bibliothèques nécessaires** : Une commande ci-dessous est prévue pour installer toutes les dépendances nécessaire.

## Guide d'installation

la commande ci dessous permet d'installer toutes les dépendances nécessaires pour ce projet :

```bash
pip install -r requirements.txt
```

## Fichiers Principaux

1. **manager_image_capture.py** : Ce fichier contient une classe `ImageCaptureSystem`, qui gère la capture des images à l'aide de la caméra Raspberri Pi V2.1, 8MP. Il inclut des fonctions pour capturer une image initiale et une image finale, ainsi qu'une fonction pour traiter et comparer ces images.

2. **image_comparison.py** : Ce fichier définit la fonction `comparer_images`, qui prend en entrée les chemins des deux images capturées. Elle utilise des techniques de traitement d'image pour calculer le score de similarité (SSIM) et le pourcentage de différence entre les images.

3. **main.py** : Ce fichier est le point d'entrée du programme, il suffit de copier et executer la commande ci-dessous pour lancer le programme :

```bash
python3 main.py
```
