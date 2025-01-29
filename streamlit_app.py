import pandas as pd
import streamlit as st
import pickle
import requests
import gdown

# Custom CSS for Styling
def local_css():
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(135deg, #1f1c2c, #928DAB);
                color: white;
                padding: 20px;
            }
            h1 {
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                color: #FF9800;
            }
            .stButton>button {
                background-color: #FF9800 !important;
                color: white !important;
                font-size: 18px !important;
                border-radius: 10px !important;
                width: 100%;
            }
            .movie-title {
                font-size: 16px;
                font-weight: bold;
                text-align: center;
            }
            label {
                color: white !important;
                font-size: 18px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Load custom styling
local_css()

# Function to download pickle file from Google Drive
def download_pickle_file():
    url = 'https://drive.google.com/uc?export=download&id=1ryKP6k1EYdBUTKMThTDChFt_GRRsSj_B'
    gdown.download(url, 'similarity.pkl', quiet=False)

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=51e2c996dd88acc487acecc949148fb0&language=en-US")
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")

# Function to get recommended movies
def recommended(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    final_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
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
st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

st.markdown('<p style="color:white; font-size:18px; font-weight:bold;">📌 Select Your Favorite Movie:</p>', unsafe_allow_html=True)
selected_movie = st.selectbox("", movies["title"].values, index=None)

if st.button("🎥 Get Recommendations"):
    names, poster = recommended(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"<p class='movie-title'>{names[0]}</p>", unsafe_allow_html=True)
        st.image(poster[0])

    with col2:
        st.markdown(f"<p class='movie-title'>{names[1]}</p>", unsafe_allow_html=True)
        st.image(poster[1])

    with col3:
        st.markdown(f"<p class='movie-title'>{names[2]}</p>", unsafe_allow_html=True)
        st.image(poster[2])

    with col4:
        st.markdown(f"<p class='movie-title'>{names[3]}</p>", unsafe_allow_html=True)
        st.image(poster[3])

    with col5:
        st.markdown(f"<p class='movie-title'>{names[4]}</p>", unsafe_allow_html=True)
        st.image(poster[4])
