import streamlit as st
import requests
import json
from matplotlib import image
import requests
from PIL import Image


url = 'http://127.0.0.1:5001/api/'

st.write("Pneumonia x-ray classification")
st.markdown("### Pneumonia recognition")

# Create a file upload field
uploaded_file = st.file_uploader(
    "Choose the x-ray scan image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_data = image.imread(uploaded_file)
    j_data = json.dumps(image_data.tolist())

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=j_data, headers=headers)
    st.write(r.text)
