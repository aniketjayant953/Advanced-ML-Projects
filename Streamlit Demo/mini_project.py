import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

url = "https://raw.githubusercontent.com/Harsh1347/Streamlit/master/data/Salary_Data.csv"

data = pd.read_csv(url)

lr = LinearRegression()
x = np.array(data['YearsExperience']).reshape(-1, 1)
y = np.array(data['Salary'])
lr.fit(x, y)
st.title("Salary Predictor")

nav = st.sidebar.radio('Navigation', ['Home', 'Prediction', 'Contributor'])

if nav == "Home":
    st.image("https://miro.medium.com/max/1100/0*i-aRHjabq-7-FM5p.webp")
    if st.checkbox('Show Table'):
        st.table(data)

    graph = st.selectbox("What kind of Graph?", ['Non-Interactive', 'Interactive'])

    val = st.slider('Filter Data Using years', 0, 20, 2)
    data = data.loc[data['YearsExperience'] >= val]
    if graph == 'Non-Interactive':
        plt.figure(figsize=(10, 5))
        plt.scatter(data['YearsExperience'], data['Salary'])
        plt.ylim(0)
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.tight_layout()
        st.pyplot()

    if graph == 'Interactive':
        layout = go.Layout(
            xaxis=dict(range=[0, 16]),
            yaxis=dict(range=[0, 210000])
        )

        fig = go.Figure(data=go.Scatter(x=data['YearsExperience'], y=data['Salary'], mode='markers'), layout=layout)

        st.plotly_chart(fig)

if nav == "Prediction":
    st.header('Know Your Salary')
    val = st.number_input('Enter Your exp', 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(1, -1)
    pred = lr.predict(val)[0]

    if st.button('Predict'):
        st.success(f'Your Predicted salary is {round(pred)}')
if nav == "Contributor":
    st.header('Contribute to our dataset')
    ex = st.number_input('Enter Your Experience', 0.0, 20.0)
    sal = st.number_input('Enter Your Salary', 0.00, 1000000.00, step=1000.0)
    if st.button('Submit'):
        to_add = {"YearsExperience": ex, 'Salary': sal}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv('Salary', mode=a, header=False, index=False)
        st.success('Submitted')
