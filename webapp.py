# Run command: streamlit run "C:\Users\ishaan phaye\Desktop\VS Code\Movie Recommendation System\webapp.py"
from github import Github
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=22ba71e47d71616603bac3fb3940cb81&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/original/' + data['poster_path']

def recommend(movie):                    
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:13]    # Defines how many recommended movies data to pass through

    recommended_movies=[]
    recommended_movies_poster=[]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

g = Github("<Access Token>")
repo = g.get_user().get_repo("Movie-Recommendation-System")
movies_dict = repo.get_contents("moviesDict.pkl")
# movies_dict=pickle.load(open(r'C:\Users\ishaan phaye\Desktop\VS Code\ML Projects\moviesDict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity_pickle = repo.get_contents("movies.pkl")
# similarity=pickle.load(open(r'C:\Users\ishaan phaye\Desktop\VS Code\ML Projects\similarity.pkl','rb'))

st.title('Movie Recommendation System!!')

selected_movie_name = st.selectbox('SELECT THE MOVIE TITLE : ',movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3=st.columns(3)
    container2=st.container()
    col4,col5,col6=st.columns(3)
    container4=st.container()
    col7,col8,col9=st.columns(3)
    container6=st.container()
    col10,col11,col12=st.columns(3)
    container1=st.container()
    container3=st.container()
    container5=st.container()
    container7=st.container()
    with container1:
        with col1:
            st.subheader(names[0])
            st.image(posters[0])
        with col2:
            st.subheader(names[1])
            st.image(posters[1])
        with col3:
            st.subheader(names[2])
            st.image(posters[2])
    with container2:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
    with container3:
        with col4:
            st.subheader(names[3])
            st.image(posters[3])
        with col5:
            st.subheader(names[4])
            st.image(posters[4])
        with col6:
            st.subheader(names[5])
            st.image(posters[5])
    with container4:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
    with container5:
        with col7:
            st.subheader(names[6])
            st.image(posters[6])
        with col8:
            st.subheader(names[7])
            st.image(posters[7])
        with col9:
            st.subheader(names[8])
            st.image(posters[8])
    with container6:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
    with container7:
        with col10:
            st.subheader(names[9])
            st.image(posters[9])
        with col11:
            st.subheader(names[10])
            st.image(posters[10])
        with col12:
            st.subheader(names[11])
            st.image(posters[11])
