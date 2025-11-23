import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import numpy as np

TRAIN_PATH = "data/train"
MODEL_PATH = "models/happy_sad_model.h5"
ENCODER_PATH = "models/label_encoder.pkl"

IMG_SIZE = (128, 128)
BATCH = 32


def retrain_model():
    """
    Retrain the existing Happy/Sad model using new images in data/train/.
    The function:
      - Loads existing model
      - Reloads training images (including new ones)
      - Retrains for 3 epochs
      - Saves updated model + updated label encoder
    """

    # Load training images with train / validation split
    train_gen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_data = train_gen.flow_from_directory(
        TRAIN_PATH,
        target_size=IMG_SIZE,
        batch_size=BATCH,
        class_mode="categorical",
        subset="training"
    )

    val_data = train_gen.flow_from_directory(
        TRAIN_PATH,
        target_size=IMG_SIZE,
        batch_size=BATCH,
        class_mode="categorical",
        subset="validation"
    )

    # Load the old model
    model = load_model(MODEL_PATH)

    # IMPORTANT FIX — compile model before training
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Retrain the model
    model.fit(
        train_data,
        validation_data=val_data,
        epochs=3
    )

    # Save updated model
    model.save(MODEL_PATH)

    # FIX — Save real label encoder, not a dict
    labels = list(train_data.class_indices.keys())
    encoder = LabelEncoder()
    encoder.fit(labels)
    joblib.dump(encoder, ENCODER_PATH)

    return "Retraining completed successfully!"
