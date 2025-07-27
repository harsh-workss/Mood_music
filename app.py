import keyword
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the Spofity Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="API_ID",
    client_secret="API_SECRET"
))

# Mood Keywords
mood_keywords = {
     "happy": ["happy hindi", "joyful bollywood", "upbeat hindi"],
    "sad": ["sad hindi", "emotional bollywood", "melancholy hindi"],
    "romantic": ["romantic hindi", "love bollywood", "valentine hindi"],
    "workout": ["gym hindi", "energetic bollywood", "workout india"],
    "rap": ["hindi rap", "bollywood rap", "desi hip hop"]
}

# Making UI
st.title("🎵 Mood-Based Playlist Generator")
mood = st.selectbox("How are you feeling today?", list(mood_keywords.keys()))
if st.button("Generate Playlist"):
    keyword = mood_keywords[mood]
    query = keyword[0] # Use the first Keyword
    import random
    offset = random.randint(0, 1000)
    query = f"{keyword[0]} hindi indian bollywood"
    results = sp.search(q=mood, type='track', limit=25, offset=offset,market="IN")


    st.write(f"Songs for your {mood} mood:")
    # Go through each song 
    for track in results['tracks']['items']:
        song_name = track['name']  # Get the name of the song
        artist_name = track['artists'][0]['name']  # Get the first artist's name
        spotify_link = track['external_urls']['spotify']

        # show the song details
        st.markdown(f"[{song_name} - {artist_name}]({spotify_link})")
