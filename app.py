import streamlit as st
import tensorflow as tf
import librosa
import numpy as np


# Load model
model = tf.keras.models.load_model("Speech_Emotion_Recognition.keras")

emotions = [
    "Angry",
    "Happy",
    "Sad",
    "Neutral",
    "Fear",
    "Disgust",
    "Surprise"
]

st.title("Speech Emotion Detection")

audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav"]
)

if audio_file is not None:

    st.audio(audio_file)

    y, sr = librosa.load(audio_file, sr=22050)

    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=40
    )

    mfcc = np.mean(mfcc.T, axis=0)

    mfcc = mfcc.reshape(1, 40)

    prediction = model.predict(mfcc)

    emotion = emotions[np.argmax(prediction)]

    st.success(f"Predicted Emotion: {emotion}")
    
