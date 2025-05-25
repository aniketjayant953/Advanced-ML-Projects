import streamlit as st
from db_helper import DB
import plotly.graph_objs as go
import plotly.express as px

# You need to have flights data in the Database before running this code
# flights_dataset = https://www.kaggle.com/code/abhayparashar31/flight-fare-prediction-simplest-approach/notebook
db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source', sorted(city))

    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_flights(source, destination)
        if len(results) == 0:
            st.text('No Flights Available')
        else:
            st.dataframe(results)

elif user_option == 'Analytics':
    st.title('Analytics')
    airline, freq = db.fetch_freq()

    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=freq,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    st.header("Bar Chart")
    city, freq1 = db.busy_airport()

    fig = px.bar(
        x=city,
        y=freq1
    )

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    st.header("Line Chart")
    date, freq2 = db.daily_freq()

    fig = px.line(
        x=date,
        y=freq2
    )

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    st.title('Tell About the Project')
