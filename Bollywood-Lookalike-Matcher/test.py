from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
from mtcnn import MTCNN
import cv2
from PIL import Image

feature_list = np.array(pickle.load(open('embedding.pkl', 'rb')))
filenames = pickle.load(open("filenames.pkl", 'rb'))

model = VGGFace(model="resnet50", include_top=False, input_shape=(224, 224, 3), pooling="avg")

detector = MTCNN()
# load img -> face detection and extract its features
sample_img = cv2.imread("paa.jpg")

results = detector.detect_faces(sample_img)

x, y, width, height = results[0]['box']

face = sample_img[y:y + height, x:x + width]

# extract its features
image = Image.fromarray(face)
image = image.resize((224, 224))

face_array = np.asarray(image)

face_array = face_array.astype('float32')

expanded_img = np.expand_dims(face_array, axis=0)
preprocess_img = preprocess_input(expanded_img)
results = model.predict(preprocess_img).flatten()

# find the cosine distance of current image with all the 8655 features
similarity = []
for i in range(len(feature_list)):
    similarity.append(cosine_similarity(results.reshape(1, -1), feature_list[i].reshape(1, -1))[0][0])
index_pos = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[0][0]

temp = cv2.imread(filenames[index_pos])
cv2.imshow('output', temp)
cv2.waitKey(0)
# recommend that images
