# utils.py
import unicodedata
import re
import streamlit as st
import base64
import os

MOTS_INDECENTS = [
    "merde", "putain", "con", "connard", "salop", "enculé",
    "bordel", "nique", "pute", "ta mère", "fdp"
]

def nettoyer_texte(t):
    """Supprime les accents et normalise la casse pour comparaison."""
    t = unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode("utf-8")
    return t.lower().strip()

def contient_mot_indescent(texte: str) -> bool:
    """Détecte les mots interdits dans un texte."""
    pattern = r'\b(?:' + '|'.join(re.escape(mot) for mot in MOTS_INDECENTS) + r')\b'
    return re.search(pattern, texte.lower(), re.IGNORECASE) is not None

def masquer_insultes(texte: str) -> str:
    """Remplace les insultes par des étoiles."""
    for mot in MOTS_INDECENTS:
        pattern = fr'\b{re.escape(mot)}\b'
        remplacement = mot[0] + '*' * (len(mot) - 1)
        texte = re.sub(pattern, remplacement, texte, flags=re.IGNORECASE)
    return texte

def afficher_robot_flotant():
    """Affiche le robot flottant en bas à droite de la page."""
    chemin_image = os.path.join(os.path.dirname(__file__), "data", "robot3.png")
    with open(chemin_image, "rb") as img:
        encoded_robot = base64.b64encode(img.read()).decode()
    st.markdown("""
        <style>
            .floating-robot {
                position: fixed;
                bottom: 20px;
                right: 30px;
                width: 180px;
                animation: float 3s ease-in-out infinite;
                z-index: 100;
            }
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
                100% { transform: translateY(0px); }
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown(f"<img src='data:image/png;base64,{encoded_robot}' class='floating-robot'>", unsafe_allow_html=True)
