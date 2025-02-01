import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8cf85d7d2fc618ef887358b92c2c1e9a')
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']





def recommend(movie_name):
    movie_index=movies[movies['title']==movie_name].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies_poster=[]
    recommended_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster through api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster




similarity=pickle.load(open('recommender_system/similarity.pkl','rb'))

movies_list=pickle.load(open('recommender_system/movies_dct.pkl','rb'))
movies=pd.DataFrame(movies_list)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:',movies['title'].values)


if st.button('Recommend'):
    st.write('Recommendations :')

    names,posters= recommend(selected_movie_name)

   

    col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="bottom", border=False)

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