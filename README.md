# 🎵 Music Recommendation System

A Machine Learning-based Music Recommendation System built using Python and Streamlit that suggests songs similar to a user's favorite track using content-based filtering techniques.

---

## 📌 Overview

This project recommends songs based on textual similarity between music metadata such as track names, artist names, and genres. The recommendation engine uses Natural Language Processing (NLP) techniques like TF-IDF Vectorization and Cosine Similarity to identify and rank similar songs.

The application is developed using Streamlit to provide an interactive and user-friendly interface for music discovery.

---

## 🚀 Features

- 🎶 Recommend songs based on similarity
- 🧠 Content-Based Recommendation System
- ⚡ Fast recommendation generation using cosine similarity
- 🌐 Interactive web application using Streamlit
- 📊 Efficient music metadata processing
- 🛠️ Simple and scalable architecture

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | Web Application Framework |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning Utilities |
| TF-IDF Vectorizer | Feature Extraction |
| Cosine Similarity | Similarity Calculation |

---

## 🧠 Machine Learning Workflow

The recommendation system follows a content-based filtering approach:

1. Load and preprocess the music dataset
2. Combine important song features
3. Convert textual data into numerical vectors using TF-IDF
4. Compute similarity scores using cosine similarity
5. Recommend the most similar songs to the selected track

---

## 📂 Project Structure

```bash
Music-Recommendation-system/
│
├── app.py
├── recommendation.py
├── README.md
├── requirements.txt
│
├── dataset/
│   └── tcc_ceds_music.csv
```

---

## 📊 Dataset Information

Dataset Used: `tcc_ceds_music.csv`

The dataset contains music-related metadata including:

- 🎵 Track Name
- 🎤 Artist Name
- 🎼 Genre

These features are combined and processed to generate song recommendations.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/arutlakeerthireddy-ctrl/Music-Recommendation-system.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Music-Recommendation-system
```

### 3️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 💡 Recommendation Process

The system works by:

- Extracting meaningful textual features from song metadata
- Transforming text into numerical vectors using TF-IDF
- Measuring similarity between songs using cosine similarity
- Returning the top matching recommendations

---

## 📸 Sample Recommendation

### Input

```text
Believer
```

### Recommended Songs

| Song | Artist |
|---|---|
| Thunder | Imagine Dragons |
| Demons | Imagine Dragons |
| Radioactive | Imagine Dragons |

---

## 📚 Concepts Demonstrated

- Machine Learning Fundamentals
- Recommendation Systems
- Natural Language Processing (NLP)
- Feature Engineering
- Data Preprocessing
- Cosine Similarity
- Streamlit Web App Development

---

## 🔮 Future Enhancements

- 🎵 Spotify API Integration
- 🖼️ Album Cover Display
- 🔊 Song Preview Support
- 🤖 Personalized Recommendations
- 📈 Hybrid Recommendation System
- 🌙 Improved UI/UX Design

---

## 🌐 Deployment Options

This project can be deployed using:

- Streamlit Community Cloud
- Render
- Railway
- Heroku

---

## 📦 Requirements

```text
streamlit
pandas
scikit-learn
numpy
```

---

## 👨‍💻 Author

**Arutla Keerthi Reddy**

---

## 📜 License

This project is developed for educational and learning purposes.