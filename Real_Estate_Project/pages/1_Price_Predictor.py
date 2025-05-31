import streamlit as st
import pickle
import pandas as pd
import numpy as np
import gzip
import shutil

st.set_page_config(page_title='Prediction')

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

# with open('pipeline.pkl', 'rb') as file:
#     pipeline = pickle.load(file)

# Load compressed
with gzip.open('pipeline.pkl.gz', 'rb') as f:
    pipeline = pickle.load(f)

st.markdown("<h1 style='text-align: center; color: #9C9D4B;'>Real Estate Prediction</h1>", unsafe_allow_html=True)

st.write('<h3>Enter your input</h3>', unsafe_allow_html=True)

# property_type
property_type = st.selectbox('Property Type', ['Flat', 'House'])
property_type = property_type.lower()
# sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# bedroom
bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathrooms = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))

# bathroom
balcony = st.selectbox('Number of Balcony', sorted(df['balcony'].unique().tolist()))

# agePossession
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

# built_up_area
built_up_area = float(st.number_input('Built-up Area'))

# servant room
servant_room = st.selectbox('Servant Room', ['No', 'Yes'])
if servant_room == 'Yes':
    servant_room = 1.0
else:
    servant_room = 0.0

# store_room
store_room = st.selectbox('Store Room', ['No', 'Yes'])
if store_room == 'Yes':
    store_room = 1.0
else:
    store_room = 0.0

# furnishing_type
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# Luxury_score
luxury_category = st.selectbox('Luxury', sorted(df['luxury_category'].unique().tolist()))

# floor_category
floor_category = st.selectbox('Floor', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # form a dataframe
    data = [[property_type, sector, bedrooms, bathrooms, balcony, property_age, built_up_area, servant_room, store_room,
             furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    text = 'The price of the property is between {} Cr and {} Cr'.format(round(low, 2), round(high, 2))
    # st.text(text)
    st.write('<span style="font-size:28px; font-weight: bold; color: green;">{}</span>'.format(text), unsafe_allow_html=True)
