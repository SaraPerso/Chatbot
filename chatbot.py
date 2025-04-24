# chatbot.py
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from utils import contient_mot_indescent, masquer_insultes

@st.cache_data(show_spinner="📦 Chargement des questions...")
def load_data():
    """Charge les données du fichier CSV."""
    chemin_csv = os.path.join(os.path.dirname(__file__), "data", "mon_cours.csv")
    df = pd.read_csv(chemin_csv, sep=";", encoding="utf-8")
    df.dropna(inplace=True)
    return df

def get_best_answer(question, df):
    """Trouve la réponse la plus pertinente à une question"""
    vectorizer = TfidfVectorizer()
    corpus = df["question"].tolist() + [question]
    tfidf = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    best_idx = scores.argmax()
    return df["reponse"].iloc[best_idx]

def chatbot_section():
    """Section Streamlit du chatbot"""
    st.markdown("<h1 style='color:white;'> Explorez le Commerce avec BotPro</h1>", unsafe_allow_html=True)
    st.write("Pose ta question sur le cours 👇")

    df = load_data()
    user_question = st.text_input("Ta question ici :")

    if user_question:
        if contient_mot_indescent(user_question):
            question_masquee = masquer_insultes(user_question)
            reponse = f"🚫 <strong>Ce langage n’est pas approprié</strong> dans : “{question_masquee}”.<br>Merci de rester respectueux 🙏."
        else:
            reponse = get_best_answer(user_question, df)
            reponse = f"😊 <strong>Réponse :</strong> {reponse}"
    else:
        reponse = "🤔 J’attends ta question avec impatience !"

    st.markdown(f'<div class="response-box">{reponse}</div>', unsafe_allow_html=True)
