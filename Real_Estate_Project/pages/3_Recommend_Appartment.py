import streamlit as st
import pickle
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

st.set_page_config(page_title='Recommender System')

cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

st.markdown("<h1 style='text-align: center; color: #9C9D4B;'>EstateQuest Recommender</h1>", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
pics_df = pd.read_csv('datasets/df_pics.csv')

st.markdown("<h4>Select Location and Radius</h4>", unsafe_allow_html=True)
selected_location = st.selectbox('Location', sorted(location_df.columns.tolist()))

radius = st.number_input('Radius in Km')

if st.button('Search'):
    result_search = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if not result_search.tolist():
        st.text('No Nearby Location Available')
    else:
        for key, values in result_search.to_dict().items():
            st.text("{:<25} -->  {} Kms".format(key, values))

st.markdown("<h4>Recommend Apartments</h4>", unsafe_allow_html=True)

selected_apartment = st.selectbox('Select an Apartment', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment, 6)
    property_names = recommendation_df['PropertyName'].values.tolist()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    pics = []

    for i in property_names:
        link = pics_df[pics_df['PropertyName'] == i]['Link'].values.tolist()[0]
        content = requests.get(link, headers=headers).content
        soup = BeautifulSoup(content, 'lxml')
        images = soup.findAll('img')
        pics.append(images[1]['src'])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(pics[0], caption=property_names[0])

    with col2:
        st.image(pics[1], caption=property_names[1])

    with col3:
        st.image(pics[2], caption=property_names[2])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(pics[3], caption=property_names[3])

    with col2:
        st.image(pics[4], caption=property_names[4])

    with col3:
        st.image(pics[5], caption=property_names[5])
