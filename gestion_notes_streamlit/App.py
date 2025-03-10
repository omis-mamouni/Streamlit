import streamlit as st
import pandas as pd

# Titre et logo
st.title("Application de Gestion des Notes")

try:
    st.image("gestion_notes_streamlit/Logo.webp", width=100)
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
