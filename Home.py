import pandas as pd
import numpy as np
import streamlit as st
import difflib
import gzip

def recommend_similar_movies(movie_name):
    movie_row = final_movie_data[final_movie_data['title'] == movie_name].index
    movie_index = movie_row[0]
    similar_movies = sorted(list(enumerate(movie_similarity[movie_index])),reverse=True,key = lambda x: x[1])

    return similar_movies



st.set_page_config(page_title="Movie Recommnender", page_icon="📈", layout="wide")

st.sidebar.title('Movie Recommendation System')
st.sidebar.image('Movie_logo.png')


# importing required data
final_movie_data = pd.read_pickle(open('movie_data.pkl', 'rb'))
# movie_similarity = pd.read_pickle(open('movies_similarity.pkl', 'rb'))
f = gzip.GzipFile('movie_similarity.npy.gz', "r") 
movie_similarity = np.load(f)

all_movie_names = final_movie_data['title'].tolist()

# Taking input from user
user_movie = st.text_input('Enter Movie Name')
submit_button = st.button('Submit')

if submit_button:
    similar_name_movie = difflib.get_close_matches(user_movie, all_movie_names)

    if len(similar_name_movie) == 0:
        st.header('Movie ' + user_movie + ' is not present.')
    else:
        my_movie = similar_name_movie[0]
        st.header('Similar movies for ' + my_movie ,' : ')
        similar_movies =  recommend_similar_movies(my_movie)

        for i in similar_movies[1:6]:
            st.text(final_movie_data.iloc[i[0]].title)
