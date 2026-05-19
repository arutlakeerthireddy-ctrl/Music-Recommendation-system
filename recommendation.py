import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset/tcc_ceds_music.csv")

# Display first 5 rows
print(data.head())

# Combine important features
data['combined_features'] = (
    data['genre'].fillna('') + ' ' +
    data['artist_name'].fillna('') + ' ' +
    data['track_name'].fillna('')
)

# Convert text data into vectors
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(
    data['combined_features']
)

# Calculate cosine similarity
cosine_sim = cosine_similarity(
    tfidf_matrix,
    tfidf_matrix
)

# Recommendation function
def get_recommendations(song_title, data, cosine_sim, top_n=10):

    # Find song index
    idx = data[data['track_name'] == song_title].index

    if len(idx) == 0:
        print("Song not found in dataset")
        return

    idx = idx[0]

    # Similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort songs
    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Top recommendations
    sim_scores = sim_scores[1:top_n+1]

    song_indices = [i[0] for i in sim_scores]

    recommendations = data.iloc[song_indices]

    return recommendations

# User input
song_name = input("Enter song name: ")

# Get recommendations
recommended_songs = get_recommendations(
    song_name,
    data,
    cosine_sim
)

# Print recommendations
if recommended_songs is not None:

    print("\nRecommended Songs:\n")

    print(
        recommended_songs[
            ['track_name', 'artist_name', 'genre']
        ]
    )

    # Visualization
    plt.figure(figsize=(10,6))

    sns.barplot(
        y='track_name',
        x='artist_name',
        data=recommended_songs
    )

    plt.title(
        f'Recommended Songs Similar to "{song_name}"'
    )

    plt.xlabel("Artist Name")
    plt.ylabel("Song Name")

    plt.tight_layout()
    plt.show()