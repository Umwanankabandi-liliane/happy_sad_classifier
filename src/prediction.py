import numpy as np
import joblib
from tensorflow.keras.models import load_model
from src.preprocessing import preprocess_image

MODEL_PATH = "models/happy_sad_model.h5"
ENCODER_PATH = "models/label_encoder.pkl"

model = load_model(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)   # Could be dict OR LabelEncoder object

def predict_emotion(file_path):

    # Preprocess image
    img = preprocess_image(file_path)
    preds = model.predict(np.expand_dims(img, axis=0))[0]

    class_index = np.argmax(preds)
    confidence = float(np.max(preds))

    # Case 1: encoder is a dict (normal Keras flow_from_directory)
    if isinstance(encoder, dict):
        class_name = list(encoder.keys())[list(encoder.values()).index(class_index)]

    # Case 2: encoder is LabelEncoder (has .classes_)
    else:
        class_name = encoder.classes_[class_index]

    return class_name, confidence
