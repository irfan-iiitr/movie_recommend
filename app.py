import streamlit as st
st.set_page_config(page_title="Movie Recommendation", page_icon="&#x1F50D;", layout="wide")
st.title('Movie Recommender System')

import pickle
import pandas as pd

movies_dict=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
import requests

def fetch_poster(movie_id):
    response =requests.get("https://api.themoviedb.org/3/movie/{}?api_key=475fa5362e82e81e33327afeffd480c3".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path'] ,data['homepage']

def recommend(movie):
    movie_index =movies[movies['original_title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    posters=[]
    links=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]]['original_title'])
        movie_id,link=fetch_poster(movie_id)
        posters.append(movie_id)
        links.append(link)
    return recommended_movies,posters,links

option = st.selectbox(
   "Get Recommendation of Similar Movies",
   movies['original_title'].values,
   index=None,
   placeholder="Select a movie...",
)

st.write('You selected:', option)

if st.button('Recommend'):
    name,posters,links =recommend(option)

    col1, col2, col3,col4,col5 = st.columns(5,gap="large")
    with col1:
        st.caption(name[0])
        st.markdown('''
        <a href="{}">
            <img src="{}" height="200vh" />
        </a>'''.format(links[0],posters[0]),
        unsafe_allow_html=True)

    with col2:
        st.caption(name[1])
        st.markdown('''
        <a href="{}">
            <img src="{}" height="200vh" />
        </a>'''.format(links[1],posters[1]),
        unsafe_allow_html=True)

    with col3:
        st.caption(name[2])
        st.markdown('''
        <a href="{}">
            <img src="{}" height="200vh" />
        </a>'''.format(links[2],posters[2]),
        unsafe_allow_html=True)
    
    with col4:
        st.caption(name[3])
        st.markdown('''
        <a href="{}">
            <img src="{}" height="200vh" />
        </a>'''.format(links[3],posters[3]),
        unsafe_allow_html=True)
    
    with col5:
        st.caption(name[4])
        st.markdown('''
        <a href="{}">
            <img src="{}" height="200vh" />
        </a>'''.format(links[4],posters[4]),
        unsafe_allow_html=True)


    
