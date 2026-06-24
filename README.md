# 🎤 Speech Emotion Detection Using Deep Learning

## 📌 Project Overview

Speech Emotion Detection is a Deep Learning-based application that analyzes human speech and predicts the underlying emotion expressed in the audio. This project leverages audio feature extraction techniques and a neural network model to classify emotions such as Happy, Sad, Angry, Fear, Neutral, Surprise, and Disgust.

The application provides an interactive user interface built with Streamlit, allowing users to upload audio files and instantly receive emotion predictions.

---

## 🎯 Objectives

* Detect emotions from speech signals.
* Extract meaningful audio features from speech recordings.
* Train a Deep Learning model for emotion classification.
* Provide an easy-to-use web interface for real-time predictions.
* Demonstrate the application of Artificial Intelligence in Human-Computer Interaction.

---

## 🧠 Technologies Used

### Programming Language

* Python

### Deep Learning Framework

* TensorFlow / Keras

### Audio Processing Libraries

* Librosa
* NumPy

### Frontend

* Streamlit

### Visualization

* Matplotlib
* Pandas



## 🔍 Dataset

Dataset = Toronto emotional speech set (TESS)
The model is trained using a speech emotion dataset containing audio recordings labeled with emotional categories.

Example emotions:

* Happy 😊
* Sad 😢
* Angry 😡
* Fear 😨
* Neutral 😐
* Surprise 😲
* Disgust 🤢

---

## ⚙️ Feature Extraction

Audio files are processed using Librosa to extract relevant features:

MFCC (Mel Frequency Cepstral Coefficients) features are used as input to the Deep Learning model.



## 🏗️ Model Architecture

The Speech Emotion Detection model uses a Deep Learning architecture based on neural networks.

Typical layers include:

* Input Layer
* LSTM / Dense Layers
* Dropout Layers
* Output Layer with Softmax Activation

The model is trained using categorical cross-entropy loss and optimized using Adam Optimizer.


## 📊 Workflow

```text
Audio Input
      ↓
Preprocessing
      ↓
Feature Extraction
      ↓
Deep Learning Model
      ↓
Emotion Prediction
      ↓
Result Display
```



## 👨‍💻 Author

Hem Kumar

Machine Learning Enthusiast | AI Developer

---

## 📄 License

This project is developed for educational and research purposes. Feel free to use and modify it with proper attribution.
