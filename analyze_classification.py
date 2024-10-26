import cv2
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image



def analyze_image_with_tflite(image_to_analyze, model_path):
    try:
        # Initialiser l'interpréteur TFLite
        interpreter = tf.lite.Interpreter(model_path=model_path)
        interpreter.allocate_tensors()

        # Obtenir les détails des entrées et sorties du modèle 
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        IMG_SIZE = (224, 224)

        img = image.load_img(image_to_analyze, target_size=IMG_SIZE)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Ajouter une dimension pour le batch

        # Convertir l'image en type attendu par TFLite (float32)
        img_array = img_array.astype(np.float32)

        # Faire la prédiction
        interpreter.set_tensor(input_details[0]['index'], img_array)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details[0]['index'])

        # Appliquer softmax pour obtenir des probabilités
        predictions = tf.nn.softmax(predictions)
        predicted_class_index = np.argmax(predictions, axis=-1)

        # Classes disponibles (adapter selon vos classes)
        class_names = ['autres', 'bio', 'non-bio']

        # Afficher le résultat
        print(f"Classe prédite: {class_names[predicted_class_index[0]]}")
        print(f"Probabilités: {predictions.numpy()}")

    except FileNotFoundError:
        print(f"Erreur : L'image à l'emplacement '{image_to_analyze}' n'a pas été trouvée.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de l'analyse sur l'image : {e}")
