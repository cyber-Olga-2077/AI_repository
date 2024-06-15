import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd

loaded_model = tf.keras.models.load_model('final_model.tf')

source_labels = pd.read_csv('signnames.csv')
labels_dict = source_labels.set_index('ClassId').T.to_dict(orient='list')
labels_list = [item[1][0] for item in list(labels_dict.items())]


def make_prediction(image):
    try:
        image = Image.open(image)
        image = image.convert('RGB')
        image = image.resize((32, 32))
        image = np.array(image)
        image = image / 255.0
        images = np.array([image])
        result = loaded_model.predict(images)[0]
        labels = [labels_list[i] for i in np.argsort(result)[::-1] if result[i] > 0.1]
        return [labels[0], ", ".join(labels[1:])]
    except Exception as e:
        print(e)
    return [None, None]