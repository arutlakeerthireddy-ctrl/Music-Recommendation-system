import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title
st.title("🎵 Music Recommendation System")

# Load dataset
data = pd.read_csv("dataset/tcc_ceds_music.csv")

# Combine features
data['combined_features'] = (
    data['genre'].fillna('') + ' ' +
    data['artist_name'].fillna('') + ' ' +
    data['track_name'].fillna('')
)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')

feature_vectors = vectorizer.fit_transform(
    data['combined_features']
)

# Similarity
similarity = cosine_similarity(feature_vectors)

# Recommendation function
def recommend(song_name):

    songs = data['track_name'].tolist()

    if song_name not in songs:
        return None

    index = data[data.track_name == song_name].index[0]

    similarity_scores = list(enumerate(similarity[index]))

    sorted_songs = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended = []

    for i in range(1, 11):

        song_index = sorted_songs[i][0]

        title = data.iloc[song_index]['track_name']
        artist = data.iloc[song_index]['artist_name']
        genre = data.iloc[song_index]['genre']

        recommended.append({
            'Song': title,
            'Artist': artist,
            'Genre': genre
        })

    return pd.DataFrame(recommended)

# Input
song_name = st.text_input(
    "Enter your favorite song"
)

# Button
if st.button("Recommend"):

    result = recommend(song_name)

    if result is not None:

        st.subheader("Recommended Songs")

        st.dataframe(result)

    else:
        st.error("Song not found")