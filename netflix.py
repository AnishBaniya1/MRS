#Library for creating interactive web application
# to import pkl file
import streamlit as st
import pickle
import requests 

#to add poster of the movie
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data = requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

#to load movie list file and similarity in read mode
movies = pickle.load(open("movies_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
similarity1 = pickle.load(open("similarity1.pkl",'rb'))

#to access the title of movie from pkl file
movies_list = movies['title'].values

#header for application
st.header("Movie Recommender System")

# to select movie name, a dropbox
select_value=st.selectbox("Select Movie", movies_list)

# to select recommendation type, a dropdown box
recommendation_type = st.selectbox("Select Recommendation Type", ["Genre", "Original Language"])

#this recommendation function recommends on the basis of Genre
def recommand1(movie):
    index=movies[movies['title']==movie].index[0]
    distance =sorted(list(enumerate(similarity[index])),reverse =True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# this function recommends on the basis of Original Language
def recommand2(movie):
    index=movies[movies['title']==movie].index[0]
    distance =sorted(list(enumerate(similarity1[index])),reverse =True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

#button to show recommendations
if st.button("Show Recommendation"):
   if recommendation_type == "Genre":
       movie_name, movie_poster = recommand1(select_value)
   else:
       movie_name, movie_poster = recommand2(select_value)
       
   col1,col2,col3,col4,col5=st.columns(5)
   with col1:
       st.text(movie_name[0])
       st.image(movie_poster[0])
   with col2:
       st.text(movie_name[1])
       st.image(movie_poster[1])
   with col3:
       st.text(movie_name[2])
       st.image(movie_poster[2])
   with col4:
       st.text(movie_name[3])
       st.image(movie_poster[3])
   with col5:
       st.text(movie_name[4])
       st.image(movie_poster[4])





