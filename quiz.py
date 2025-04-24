# quiz.py
import streamlit as st
import random
from chatbot import load_data
from difflib import SequenceMatcher
from utils import nettoyer_texte

def quiz_section():
    """Section Streamlit pour le quiz de révision"""
    st.header("📚 Quiz de révision")

    if "quiz_q" not in st.session_state:
        st.session_state.quiz_q = None
    if "quiz_done" not in st.session_state:
        st.session_state.quiz_done = False
    if "reponse_libre" not in st.session_state:
        st.session_state.reponse_libre = ""
    if "selected_qcm" not in st.session_state:
        st.session_state.selected_qcm = None
    if "next_question" not in st.session_state:
        st.session_state.next_question = False
    if "propositions" not in st.session_state:
        st.session_state.propositions = None

    df = load_data()

    if st.session_state.quiz_q is None or st.session_state.next_question:
        st.session_state.quiz_q = random.choice(df.to_dict("records"))
        st.session_state.quiz_done = False
        st.session_state.reponse_libre = ""
        st.session_state.selected_qcm = None
        st.session_state.propositions = None
        st.session_state.next_question = False

    question = st.session_state.quiz_q["question"]
    reponse_attendue = st.session_state.quiz_q["reponse"]

    st.subheader(f"🤔 {question}")

    reponse_libre = st.text_input(
        "💬 Ta réponse :",
        value=st.session_state.reponse_libre,
        key="reponse_libre",
        placeholder="Appuie sur Entrée pour valider..."
    )

    if st.session_state.propositions is None or st.session_state.quiz_done:
        propositions = [reponse_attendue]
        while len(propositions) < 4:
            r = random.choice(df["reponse"].tolist())
            if r not in propositions:
                propositions.append(r)
        random.shuffle(propositions)
        st.session_state.propositions = propositions

    choix_qcm = st.radio(
        "☑️ Ou choisis une réponse:",
        st.session_state.propositions,
        key="choix_qcm",
        index=None
    )

    if st.button("✅ Valider la réponse"):
        if reponse_libre.strip() and choix_qcm:
            st.warning("❗Merci de répondre soit à la question libre, soit au QCM, pas les deux.")
        elif reponse_libre.strip():
            ratio = SequenceMatcher(None, nettoyer_texte(reponse_attendue), nettoyer_texte(reponse_libre)).ratio()
            if ratio > 0.6:
                st.success("✅ Bonne réponse !")
                st.session_state.quiz_done = True
            else:
                st.error(f"❌ Mauvaise réponse. Réponse attendue : {reponse_attendue}")
        elif choix_qcm:
            if choix_qcm == reponse_attendue:
                st.success("✅ Bonne réponse !")
                st.session_state.quiz_done = True
            else:
                st.error(f"❌ Mauvaise réponse. Réponse attendue : {reponse_attendue}")
        else:
            st.warning("❗Merci de répondre à la question ou de choisir une réponse dans le QCM.")

    if st.session_state.quiz_done:
        if st.button("🔁 Question suivante"):
            st.session_state.next_question = True
            st.rerun()

def jeu_cinq_mots_section():
    """Section Streamlit pour le
