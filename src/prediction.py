import numpy as np
from src.preprocessing import preprocess_image
from src.model import load_classifier

# Load model + encoder once (faster)
model, encoder = load_classifier()

def predict_emotion(image_path):
    """
    Predict whether an image is 'happy' or 'sad'.
    Returns:
      - label (happy/sad)
      - confidence score
    """
    img = preprocess_image(image_path)
    preds = model.predict(img)
    
    class_index = np.argmax(preds)
    
    # Convert class index → class name using encoder dictionary
    class_name = list(encoder.keys())[list(encoder.values()).index(class_index)]

    return class_name, float(np.max(preds))
