import streamlit as st
import requests
import json
from matplotlib import image
import requests
from PIL import Image
import numpy as np
from skimage import transform
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout, BatchNormalization
import tensorflow as tf


def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), strides=1, padding='same',
                     activation='relu', input_shape=(150, 150, 1)))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding='same'))
    model.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu'))
    model.add(Dropout(0.1))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding='same'))
    model.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding='same'))
    model.add(Conv2D(128, (3, 3), strides=1, padding='same', activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding='same'))
    model.add(Conv2D(256, (3, 3), strides=1, padding='same', activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding='same'))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(optimizer="rmsprop",
                  loss='binary_crossentropy', metrics=['accuracy'])
    return model


def preprocess(np_image):
    np_image = Image.open(np_image)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (150, 150, 1))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


def get_prediction(img_path):
    '''
        This function takes as an input the image path
        and return the model prediction for this image ['PNEUMONIA', 'NORMAL']
        This model is trained on this dataset: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
    '''
    img = preprocess(img_path)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        return 'Normal'

    return 'Pneumonia'


st.write("Pneumonia x-ray classification")
st.markdown("### Pneumonia recognition")
model = tf.keras.models.load_model(
    r'/app/pneumonia-x-ray-classification/deployment/streamlit/my_model.h5')
# Create a file upload field
uploaded_file = st.file_uploader(
    "Choose the x-ray scan image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.write(get_prediction(uploaded_file))
