# streamlit_app.py  
# -----------------------------------------
# This script is the Streamlit web interface for the Movie Recommender System.
# It provides an interactive platform for users to input a movie title and receive 
# recommendations directly on their browser.  
#
# To run this application, execute the following command in the terminal:
#  
#     streamlit run streamlit_app.py  
#
# Once executed, Streamlit will launch the app in your default web browser.
# -----------------------------------------

import pandas as pd
import streamlit as st
import pickle
import requests
import gdown

# Function to download pickle file from Google Drive
def download_pickle_file():
    url = 'https://drive.google.com/uc?export=download&id=1ryKP6k1EYdBUTKMThTDChFt_GRRsSj_B'  # Use the direct link to your file
    gdown.download(url, 'similarity.pkl', quiet=False)

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=51e2c996dd88acc487acecc949148fb0&language=en-US")
    data = response.json()
    return  "http://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommended(movie):
    movie_index = movies[movies["title"] == movie ].index[0]
    distance = similarity[movie_index]
    final_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for j in final_movies:
        movies_id = movies.iloc[j[0]].movie_id
        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movies_poster.append(fetch_poster(movies_id))
    return recommended_movies, recommended_movies_poster

# Download the similarity pickle file
download_pickle_file()

# Load the data
movies_list = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies_list)

# Load the similarity model
similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit UI
st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Select your Favourite Movie here:",
    movies["title"].values,
    index=None,
)

if st.button("Recommended"):
    names, poster = recommended(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
