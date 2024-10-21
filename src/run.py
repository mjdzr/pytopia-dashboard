# Import necessary libraries
import streamlit as st
import json
import importlib.util
from PIL import Image

# Page header
banner = Image.open('input/banner.png')
st.image(banner, use_column_width=True)
st.title(':musical_note: Spotify Song Search')

# Load the good.json file
with open('input/good.json', 'r') as f:
    data = json.load(f)

# Load the yes.py file from input folder
spec = importlib.util.spec_from_file_location("yes", 'input/yes.py')
yes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(yes)

# Initialize a list to store the matching song names
song_names = []

# Extract matching song names
for message in data['audio_features']:
    for track in yes.yes_ids['items']:
        if message['id'] == track['track']['id']:
            song_names.append(track['track']['name'])

# Add a search box for filtering song names
search_term = st.text_input("Search for a song")

# Filter the song names based on the search term
if search_term:
    filtered_songs = [name for name in song_names if search_term.lower() in name.lower()]
    songs_to_display = filtered_songs  # Only display filtered songs if search is active
else:
    songs_to_display = song_names  # Display all songs if no search term is entered

# Display the total number of songs (filtered or not)
st.write(f"Total Songs: {len(songs_to_display)}")

# Initialize session state for pagination
if 'page' not in st.session_state:
    st.session_state.page = 0

# Define the number of songs per page
SONGS_PER_PAGE = 10

# Display songs in a collapsible section with pagination
start_index = st.session_state.page * SONGS_PER_PAGE
end_index = start_index + SONGS_PER_PAGE

with st.expander("Song Titles", expanded=True):
    for song in songs_to_display[start_index:end_index]:
        st.write(f"- {song}")

# Add Next and Previous buttons for pagination
col1, col2 = st.columns([1, 1])

if col1.button("Previous") and st.session_state.page > 0:
    st.session_state.page -= 1

if col2.button("Next") and end_index < len(songs_to_display):
    st.session_state.page += 1

# Login or sign-up
login_option = st.sidebar.radio('Login or Sign Up', ['login', 'sign up'])

if login_option == 'login':
    with st.sidebar.form("login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("login")
        if submitted:
            pass  # Add your login logic here
else:
    with st.sidebar.form("sign up"):
        st.write("Sign Up Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        submitted = st.form_submit_button("sign up")
        if submitted:
            pass  # Add your signup logic here



