'''
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Charger le modèle TFLite
tflite_model_path = '/home/judicael/Systeme-intelligent-de-tri-des-dechets-menagers/my_model/classification_dechets_ameliore_v2.tflite'

# Initialiser l'interpréteur TFLite
interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

# Obtenir les détails des entrées et sorties du modèle
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prétraiter l'image pour le modèle
IMG_SIZE = (224, 224)
image_path = "/home/judicael/Systeme-intelligent-de-tri-des-dechets-menagers/captured_image4.jpg"

img = image.load_img(image_path, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension pour le batch

# Convertir l'image en type attendu par TFLite (float32)
img_array = img_array.astype(np.float32)

# Prédiction
interpreter.set_tensor(input_details[0]['index'], img_array)
interpreter.invoke()
predictions = interpreter.get_tensor(output_details[0]['index'])

# Appliquer la fonction softmax pour obtenir des probabilités
predictions = tf.nn.softmax(predictions)
predicted_class_index = np.argmax(predictions, axis=-1)[0]

# Classes disponibles
class_names = ['autres', 'bio', 'non-bio']

# Afficher le résultat
print(f"Classe prédite: {class_names[predicted_class_index]}")
print(f"Probabilités: {predictions.numpy()}")
'''

import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image



def analyze_image_with_tflite(image_to_analyze, model_path):
    try:
        # Charger les deux images
        imag = cv2.imread(image_to_analyze)
        # Initialiser l'interpréteur TFLite
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()

        # Obtenir les détails des entrées et sorties du modèle 
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        IMG_SIZE = (224, 224)

        img = image.load_img(imag       , target_size=IMG_SIZE)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension pour le batch

        # Convertir l'image en type attendu par TFLite (float32)
        img_array = img_array.astype(np.float32)

        # Faire la prédiction
        interpreter.set_tensor(input_details['index'], img_array)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details['index'])

        # Appliquer softmax pour obtenir des probabilités
        predictions = tf.nn.softmax(predictions)
        predicted_class_index = np.argmax(predictions, axis=-1)

        # Classes disponibles (adapter selon vos classes)
        class_names = ['autres', 'bio', 'non-bio']

        # Afficher le résultat
        print(f"Classe prédite: {class_names[predicted_class_index]}")
        print(f"Probabilités: {predictions.numpy()}")

    except FileNotFoundError:
        print(f"Erreur : L'image à l'emplacement '{image_to_analyze}' n'a pas été trouvée.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de l'analyse sur l'image : {e}")
