# database.py
import sqlite3
from datetime import datetime

def init_database():
    """Initialise la base de données des visites"""
    conn = sqlite3.connect('visites.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS visites 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  date TEXT)''')
    conn.commit()
    conn.close()

def enregistrer_visite():
    """Enregistre une nouvelle visite"""
    conn = sqlite3.connect('visites.db')
    c = conn.cursor()
    date_heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO visites (date) VALUES (?)", (date_heure,))
    conn.commit()
    conn.close()

def total_visites():
    """Récupère le nombre total de visites"""
    conn = sqlite3.connect('visites.db')
    c = conn.cursor()
    total = c.execute("SELECT COUNT(*) FROM visites").fetchone()[0]
    conn.close()
    return total
