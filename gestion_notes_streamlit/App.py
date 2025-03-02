import streamlit as st
import pandas as pd

# Liste pour stocker les données
data = []

# Titre et logo
st.title("Application de Gestion des Notes")
st.image("Logo.jpeg", width=100)  # Remplacez par le chemin de votre logo

# Formulaire pour saisir les informations
with st.form("formulaire_note"):
    nom_prenom = st.text_input("Nom & Prénom")
    module = st.text_input("Module")
    note = st.number_input("Note finale", min_value=0, max_value=20)
    
    # Bouton pour enregistrer
    submitted = st.form_submit_button("Enregistrer")
    
    if submitted:
        # Enregistrer les données dans la liste
        data.append([nom_prenom, module, note])
        st.success("Les informations ont été enregistrées!")

# Convertir la liste en DataFrame pour l'afficher dans un tableau
df = pd.DataFrame(data, columns=["Nom & Prénom", "Module", "Note finale"])

# Afficher le tableau dynamique
if len(data) > 0:
    st.write("Voici toutes les entrées enregistrées :")
    st.dataframe(df)
else:
    st.write("Aucune entrée n'a encore été enregistrée.")

