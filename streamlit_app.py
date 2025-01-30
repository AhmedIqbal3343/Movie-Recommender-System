import pandas as pd
import streamlit as st
import pickle
import requests
import gdown

# Function to download pickle file from Google Drive (only if not available)
@st.cache_data
def download_pickle_file():
    url = 'https://drive.google.com/uc?export=download&id=1ryKP6k1EYdBUTKMThTDChFt_GRRsSj_B'  
    gdown.download(url, 'similarity.pkl', quiet=False)

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=51e2c996dd88acc487acecc949148fb0&language=en-US")
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")

# Function to get movie recommendations
def recommended(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    final_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for j in final_movies:
        movie_id = movies.iloc[j[0]].movie_id
        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

# Caching movie data
@st.cache_data
def load_movies():
    return pickle.load(open("movies.pkl", "rb"))

@st.cache_data
def load_similarity():
    return pickle.load(open("similarity.pkl", "rb"))

# Download similarity file if not present
download_pickle_file()

# Load movies and similarity matrix once
if "movies" not in st.session_state:
    st.session_state.movies = pd.DataFrame(load_movies())

if "similarity" not in st.session_state:
    st.session_state.similarity = load_similarity()

movies = st.session_state.movies
similarity = st.session_state.similarity

# Streamlit UI
st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Select your Favourite Movie here:",
    movies["title"].values
)

if st.button("Recommend"):
    names, posters = recommended(selected_movie)
    cols = st.columns(5)
    
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
