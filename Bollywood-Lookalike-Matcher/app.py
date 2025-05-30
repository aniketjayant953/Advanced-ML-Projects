import os
import streamlit as st
from PIL import Image
import cv2
from mtcnn import MTCNN
import numpy as np
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from sklearn.metrics.pairwise import cosine_similarity
import pickle

model = VGGFace(model="resnet50", include_top=False, input_shape=(224, 224, 3), pooling="avg")
detector = MTCNN()
feature_list = pickle.load(open('embedding.pkl', 'rb'))
filename = pickle.load(open('filenames.pkl', 'rb'))


def save_uploaded_image(uploaded_image):
    try:
        with open(os.path.join('uploads', uploaded_image.name), 'wb') as f:
            f.write(uploaded_image.getbuffer())
            return True
    except:
        return False


def extract_features(img_path, model, detector):
    img = cv2.imread(img_path)
    results = detector.detect_faces(img)

    x, y, width, height = results[0]['box']

    face = img[y:y + height, x:x + width]

    # extract its features
    image = Image.fromarray(face)
    image = image.resize((224, 224))

    face_array = np.asarray(image)

    face_array = face_array.astype('float32')

    expanded_img = np.expand_dims(face_array, axis=0)
    preprocess_img = preprocess_input(expanded_img)
    results = model.predict(preprocess_img).flatten()

    return results


def recommend(feature_list, features):
    similarity = []
    for i in range(len(feature_list)):
        similarity.append(cosine_similarity(features.reshape(1, -1), feature_list[i].reshape(1, -1))[0][0])
    index_pos = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[0][0]

    return index_pos


st.title("Which Bollywood Celebrity are You?")

uploaded_image = st.file_uploader('Choose an image')

if uploaded_image is not None:
    # save the image in a directory
    if save_uploaded_image(uploaded_image):
        # load the image
        display_image = Image.open(uploaded_image)

        # extract the features
        features = extract_features(os.path.join('uploads', uploaded_image.name), model, detector)
        # recommend
        index_pos = recommend(feature_list, features)
        predicted_actor = " ".join(filename[index_pos].split('\\')[1].split('_'))

        # display
        co1, col2 = st.columns(2)
        with co1:
            # st.header('Your uploaded image')
            st.markdown("<h4 style='color:white;'>Your uploaded image</h4>", unsafe_allow_html=True)
            st.write()
            st.image(display_image, width=300)
        with col2:
            # st.header('Your Bollywood Lookalike is {}'.format(predicted_actor))
            st.markdown("<h4 style='color:white;'>Your Bollywood Lookalike is {}</h4>".format(predicted_actor), unsafe_allow_html=True)
            st.write()
            st.image(filename[index_pos], width=300)
