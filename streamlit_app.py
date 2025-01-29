import pandas as pd
import streamlit as st
import pickle
import requests


# Load Data
@st.cache_data
def load_data():
    movies_list = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return pd.DataFrame(movies_list), similarity


movies, similarity = load_data()


# Fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=51e2c996dd88acc487acecc949148fb0&language=en-US"
    )
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data.get("poster_path", "")


# Recommendation function
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


# UI Styling
st.markdown(
    """
    <style>
        /* Background with gradient */
        .stApp {
            background: linear-gradient(135deg, #1F1C2C, #3A1C71, #D76D77, #FFAF7B);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: white !important;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Movie selection text */
        .stSelectbox label {
            color: white !important; 
            font-weight: bold;
            font-size: 20px;
        }

        /* Button styling */
        .stButton>button {
            color: white !important;
            background: linear-gradient(45deg, #FF512F, #DD2476);
            border-radius: 10px;
            padding: 12px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #DD2476, #FF512F);
            transform: scale(1.05);
        }

        /* Main title styling */
        .stTitle {
            color: white !important;
        }

        /* Specific styling for the title */
        h1 {
            color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Movie Recommender System")

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

selected_movie = st.selectbox(
    "📌 Select Your Favorite Movie:",
    movies["title"].values,
    index=None,
    key="selected_movie"
)

if st.button("🎥 Get Recommendations"):
    if selected_movie:
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
