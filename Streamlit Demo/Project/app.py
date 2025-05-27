import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('startup_cleaned.csv')


def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())

    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # average ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    col1, col2, col3, col4 = st.columns(4)

    # total funded statups
    num_startup = len(df['startup'].unique())

    with col1:
        st.metric('Total', str(total) + 'Cr')
    with col2:
        st.metric('Max funding', str(max_funding) + 'Cr')

    with col3:
        st.metric('Avg funding', str(round(avg_funding)) + 'Cr')
    with col4:
        st.metric('Funded startups', str(num_startup) + 'Startups')

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()

    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()
    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig3)


def load_investors_details(investor):
    st.title(investor)
    # load 5 investments of the investors
    last5_inv = df[df['investors'].str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_inv)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investment
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head(5)
        st.subheader('Biggest Investments')

        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col2:
        # pie chart
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sector invested in ')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f%%')
        st.pyplot(fig1)

    years_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YoY Investments')

    fig2, ax2 = plt.subplots()
    ax2.plot(years_series.index, years_series.values)
    st.pyplot(fig2)


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    st.title('Startup Analysis')
    btn1 = st.sidebar.button('Find StartUp Details')
else:
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(',').sum())))
    st.title('Investor Analysis')
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        load_investors_details(selected_investor)
