from fastapi import FastAPI, UploadFile, File
import shutil
import uuid
import os

from src.prediction import predict_emotion
from src.retraining import retrain_model

app = FastAPI(title="Happy Sad Classifier API")

# Create uploads directory if not exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Happy-Sad Classifier API is running!"}


@app.post("/predict")
def predict(file: UploadFile = File(...)):
    """
    Upload an image and return happy/sad prediction.
    """
    # Save uploaded image temporarily
    file_id = f"{UPLOAD_DIR}/{uuid.uuid4()}.jpg"
    with open(file_id, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get prediction
    label, confidence = predict_emotion(file_id)

    return {
        "prediction": label,
        "confidence": round(confidence, 4)
    }


@app.post("/retrain")
def retrain():
    """
    Trigger model retraining using data in data/train/
    """
    message = retrain_model()
    return {"message": message}
