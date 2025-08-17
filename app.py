import pickle
import streamlit as st
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
get_song_album_cover_url = ''
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names ,recommended_music_posters
def recommend(song, music, similarity):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    for i in distances[1:6]:
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names 

st.header('Music Recommender System')
music = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox("choose your favorite song ",music_list)

if st.button('Show Recommendation'):
    recommended_music_names = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
       # st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
       # st.image(recommended_music_posters[1])

    with col3:
        st.text(recommended_music_names[2])
       # st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
       # st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        #st.image(recommended_music_posters[4])
    



