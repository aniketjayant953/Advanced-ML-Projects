import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import ast

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title='Plotting', layout="wide")

# Importing Datasets
wc_df = pd.read_csv('datasets/wc_df.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))
new_df = pd.read_csv('datasets/data_viz1.csv')

# Title
st.markdown("<h1 style='text-align: center; color: #9C9D4B;'>Real Estate Analytics</h1>", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)

# World Map
group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()

st.markdown("<h4>Sector Price per Sqft Geomap</h4>", unsafe_allow_html=True)
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map", width=1200, height=700, hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

# WordCloud
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h4>Facilities/Amenities WordCould</h4>", unsafe_allow_html=True)

    sectors = new_df['sector'].unique().tolist()
    sectors.insert(0, 'Overall')
    sectors.sort()

    sector_wc = st.selectbox('Select Sector', [i.capitalize() for i in sectors])

    if sector_wc == 'Overall':
        wordcloud = WordCloud(width=800, height=800,
                              background_color='black',
                              stopwords=set(['s']),  # Any stopwords you'd like to exclude
                              min_font_size=10).generate(feature_text)

        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot()
    else:
        features = wc_df[wc_df['sector'] == sector_wc.lower()]['features'].dropna()

        wc_text = []
        for i in features.apply(ast.literal_eval):
            wc_text.extend(i)

        feature_text_filtered = " ".join(wc_text)

        wordcloud = WordCloud(width=800, height=800,
                              background_color='black',
                              stopwords=set(['s']),  # Any stopwords you'd like to exclude
                              min_font_size=10).generate(feature_text_filtered)

        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot()

# Pie Chart
with col2:
    st.markdown("<h4>BHK Pie Chart</h4>", unsafe_allow_html=True)

    selected_sector = st.selectbox('Choose Sector', [i.capitalize() for i in sectors])

    if selected_sector == 'Overall':

        fig2 = px.pie(new_df, names='bedRoom')

        st.plotly_chart(fig2, use_container_width=True)
    else:

        fig2 = px.pie(new_df[new_df['sector'] == selected_sector.lower()], names='bedRoom')

        st.plotly_chart(fig2, use_container_width=True)

# ScatterPlot
st.markdown("<h4>Area Vs Price</h4>", unsafe_allow_html=True)

property_type = st.selectbox('Select Property Type', ['Flat', 'House'])

if property_type == 'House':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom",
                      labels={'built_up_area': 'Built-Up Area', 'price': 'Price'})

    # Show the plot
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      labels={'built_up_area': 'Built-Up Area', 'price': 'Price'})

    # Show the plot
    st.plotly_chart(fig1, use_container_width=True)

# BoxPlot
st.markdown("<h4>Side by Side BHK price comparison</h4>", unsafe_allow_html=True)

bhk_df = new_df[new_df['bedRoom'] <= 4]
fig3 = px.box(bhk_df, x='bedRoom', y='price', color='property_type', labels={'bedRoom': 'Bed Room', 'price': 'Price'})
st.plotly_chart(fig3, use_container_width=True)

# Density Plot
st.markdown("<h4>Side by Side Distribution plot for property type</h4>", unsafe_allow_html=True)

# Add density data
x1 = (new_df[new_df['property_type'] == 'house']['price']).tolist()
x2 = (new_df[new_df['property_type'] == 'flat']['price']).tolist()

# Group data together
hist_data = [x1, x2]

group_labels = ['House', 'Flat']

# Create distplot with custom bin_size
fig5 = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5], show_rug=False)

# Plot!
st.plotly_chart(fig5, use_container_width=True)
