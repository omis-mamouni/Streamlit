import streamlit as st
import pandas as pd

import os

# Afficher les fichiers disponibles dans le répertoire courant
st.write("Fichiers dans le dossier :", os.listdir())

# Vérifier si le fichier existe
logo_path = "gestion_notes_streamlit/Logo.webp"

if os.path.exists(logo_path):
    st.success(f"Le fichier {logo_path} existe.")
    st.image(logo_path, width=100)
else:
    st.error(f"⚠ Le fichier {logo_path} est introuvable dans le dossier actuel.")

# Initialiser la session pour stocker les données de manière temporaire
if "data" not in st.session_state:
    st.session_state.data = []

# Titre et logo
st.title("Application de Gestion des Notes")

try:
    st.image("Logo.webp")
except Exception as e:
    st.error(f"Erreur lors de l'affichage du logo : {e}")

# Formulaire pour saisir les informations
with st.form("formulaire_note"):
    nom_prenom = st.text_input("Nom & Prénom")
    module = st.text_input("Module")
    note = st.number_input("Note finale", min_value=0, max_value=20)
    
    submitted = st.form_submit_button("Enregistrer")

    if submitted:
        if nom_prenom and module:  # Vérification que les champs ne sont pas vides
            st.session_state.data.append([nom_prenom, module, note])
            st.success("Les informations ont été enregistrées!")
        else:
            st.warning("Veuillez remplir tous les champs.")

# Convertir en DataFrame
df = pd.DataFrame(st.session_state.data, columns=["Nom & Prénom", "Module", "Note finale"])

# Afficher les notes enregistrées
if not df.empty:
    st.write("Voici toutes les entrées enregistrées :")
    st.dataframe(df)
else:
    st.write("Aucune entrée n'a encore été enregistrée.")
