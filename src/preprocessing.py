import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

IMG_SIZE = (128, 128)

def preprocess_image(image_path):
    """
    Load and preprocess an image for prediction.
    - Resize to 128x128
    - Normalize pixels
    - Convert to array
    """
    img = cv2.imread(image_path)
    img = cv2.resize(img, IMG_SIZE)
    img = img.astype("float") / 255.0
    img = img_to_array(img)
    return np.expand_dims(img, axis=0)
