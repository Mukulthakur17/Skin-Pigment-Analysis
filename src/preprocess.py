from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow.keras.models as models

def predict(temp_file):
    test_image = image.load_img(temp_file, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    with open('Model Weights _ Json/model.json','r') as json_file:
        json_model = json_file.read()
    model = model_from_json(json_model)
    model.load_weights('Model Weights _ Json/model_weights.h5')
    result = model.predict(test_image)
    return np.argmax(result)
