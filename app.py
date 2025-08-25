import keyword
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import joblib
import random

# Set up Spotify Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="129fcb6e799040f880e9a4d5129b6561",
    client_secret="bac93bb269ae4218b6829ef94a3d1839"
))

# Load the model
model = joblib.load("saved_models/mood_model.pkl")

# Mood Keywords
mood_keywords = {
    "happy": ["happy hindi", "joyful bollywood", "upbeat hindi"],
    "sad": ["sad hindi", "emotional bollywood", "melancholy hindi"],
    "romantic": ["romantic hindi", "love bollywood", "valentine hindi"],
    "workout": ["gym hindi", "energetic bollywood", "workout india"],
    "rap": ["hindi rap", "bollywood rap", "desi hip hop"]
}

# Streamlit UI
st.title("🎵 Mood-Based Playlist Generator")

# User input
user_input = st.text_input("Enter a song lyric, feeling, or text to detect mood:")

if st.button("Generate Playlist", key="playlist_button"):
    if user_input.strip() != "":
        # Step 1: Predict mood
        pred = model.predict([user_input])[0]
        st.write(f"✅ Detected mood: **{pred}**")

        # Step 2: Use detected mood to fetch songs
        if pred in mood_keywords:
            keyword = random.choice(mood_keywords[pred])  # Pick a random keyword for variety
            offset = random.randint(0, 500)  # Randomize search results
            results = sp.search(q=f"{keyword} hindi bollywood", type="track", limit=15, offset=offset, market="IN")

            st.write(f"🎶 Songs for your **{pred}** mood:")

            # Show songs
            for track in results['tracks']['items']:
                song_name = track['name']
                artist_name = track['artists'][0]['name']
                spotify_link = track['external_urls']['spotify']
                st.markdown(f"[{song_name} - {artist_name}]({spotify_link})")
        else:
            st.warning("😕 Sorry, I don’t have recommendations for this mood yet.")
