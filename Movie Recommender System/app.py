import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=27ab3dcd7a81e9b7ef0a93efe00b933e&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    tmdb_path = 'https://image.tmdb.org/t/p/w500/'
    return tmdb_path + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    similar = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in similar:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Show me Recommendations",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
