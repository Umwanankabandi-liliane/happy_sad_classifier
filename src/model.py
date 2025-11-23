from tensorflow.keras.models import load_model
import joblib

MODEL_PATH = "models/happy_sad_model.h5"
ENCODER_PATH = "models/label_encoder.pkl"

def load_classifier():
    """
    Load the trained model + label encoder.
    """
    model = load_model(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder
