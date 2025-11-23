import streamlit as st
import requests
from PIL import Image
import io

# Replace this with your deployed API URL on Render later:
API_URL = "http://localhost:8000"

st.title("😊 Happy vs Sad Face Classifier 😢")
st.write("Upload an image and let the model predict the emotion.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    # Send image to API
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    files = {"file": ("uploaded.jpg", img_bytes, "image/jpeg")}

    with st.spinner("Predicting..."):
        response = requests.post(f"{API_URL}/predict", files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: **{result['prediction'].upper()}**")
        st.write(f"Confidence: **{result['confidence']}**")
    else:
        st.error("Prediction failed. Check API connection.")


st.subheader("🔁 Retrain Model")
st.write("Upload more training images into `/data/train/` and press the button below.")

if st.button("Start Retraining"):
    with st.spinner("Retraining the model..."):
        res = requests.post(f"{API_URL}/retrain")

    st.success(res.json())
