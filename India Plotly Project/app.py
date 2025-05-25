import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('india.csv')
uni_states = list(df['State'].unique())
uni_states.insert(0, 'All')

st.set_page_config(layout='wide')

st.sidebar.title('India ka Data Visualization')

selected_state = st.sidebar.selectbox('Select a State', uni_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Secondary Primary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'All':
        # plot india
        st.text(f'Size represent {primary}')
        st.text(f'Color represent {secondary}')
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=4, width=1200,
                                height=700, hover_name='District',
                                mapbox_style='carto-positron')
        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        st.text(f'Size represent {primary}')
        st.text(f'Color represent {secondary}')

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=4, width=1200,
                                height=700, hover_name='District',
                                mapbox_style='carto-positron')
        st.plotly_chart(fig, use_container_width=True)
