# app.py
import streamlit as st
from database import init_database, enregistrer_visite, total_visites
from chatbot import chatbot_section
from quiz import quiz_section, jeu_cinq_mots_section
from utils import afficher_robot_flotant

# Initialisation base de données
init_database()

st.set_page_config(page_title="Chatbot LycéePro", layout="centered")

# Enregistrement de la visite
if "visite_loggee" not in st.session_state:
    st.session_state.visite_loggee = True
    enregistrer_visite()

total = total_visites()
if total >= 300:
    st.toast("🥳 Déjà plus de 300 visites ! Merci !")

# Affichage robot
afficher_robot_flotant()

# Interface
col1, col2 = st.columns([0.15, 0.85])
with col1:
    st.image("data/robot-assistant.png", width=200)
with col2:
    st.markdown("<h1 style='color: white; padding-top:40px;'> Bienvenue sur BotPro</h1>", unsafe_allow_html=True)

st.markdown("<div class='main-title'> L’assistant virtuel pour les cours des Métiers du commerce et de la vente</div>", unsafe_allow_html=True)

# Navigation
onglets = st.tabs(["🤖 Chatbot", "🎯 Quiz de révision", "🎮 Jeu des 5 mots", "📚 Digipad"])

with onglets[0]:
    chatbot_section()

with onglets[1]:
    quiz_section()

with onglets[2]:
    jeu_cinq_mots_section()

with onglets[3]:
    st.header("📚 Accès au Digipad")
    st.markdown("""
    <iframe src="https://digipad.app/p/847630/15248ba9144b5" width="100%" height="850px" style="border: none; border-radius: 12px;"></iframe>
    """, unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div style='text-align: center; font-size: 1em; color: white; margin-top: 40px; padding-top: 20px;'>
    ✨ Crois en toi, révise avec le sourire 😄 et donne le meilleur de toi-même !<br>
        💪 Bon courage pour tes révisions !<br><br>
        👉 <a href="https://digipad.app/p/847630/15248ba9144b5" target="_blank" style="color:white; font-weight:bold;">
        Accède ici à ton Digipad 📚</a><br><br>
    👥 <strong>Nombre total de visiteurs :</strong> {total}
</div>
""", unsafe_allow_html=True)

# Signature personnalisée en bas à droite
st.markdown(
    """
    <div style='text-align: right; font-size: 0.9em; color: white; margin-top: 30px;'>
        Réalisé par <strong>Sarah Ouziel</strong> © 2025
    </div>
    """,
    unsafe_allow_html=True
)

# 📆 Badge de mise à jour
from datetime import datetime
date_maj = datetime.now().strftime("%d/%m/%Y à %Hh%M")
st.markdown(
    f"""
    <div style='text-align: center; font-size: 0.9em; color: white; margin-top: 10px;'>
        📆 Dernière mise à jour : <strong>{date_maj}</strong>
    </div>
    """,
    unsafe_allow_html=True
)
