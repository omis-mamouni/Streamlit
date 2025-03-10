import streamlit as st
import pandas as pd

# Affichage du logo avec un petit coup de propre
st.markdown(
    """
    <div style="text-align: center;">
        <img src="gestion_notes_streamlit/Logo.webp" width="100">
    </div>
    """,
    unsafe_allow_html=True
)

# Un bon titre pour mettre les choses en place
st.title("📚 Application de Gestion des Notes")

# Vérification de l'existence de `st.session_state.data`, sinon on l'initialise
if "data" not in st.session_state:
    st.session_state.data = []

# Un petit message pour guider l'utilisateur
st.write("Veuillez remplir le formulaire ci-dessous pour enregistrer une note.")

# Formulaire d'ajout d'une note
with st.form("formulaire_note"):
    nom_prenom = st.text_input("✍️ Nom & Prénom", placeholder="Entrez votre nom complet")
    module = st.text_input("📖 Module", placeholder="Ex : Mathématiques, Informatique...")
    note = st.number_input("🎯 Note finale", min_value=0, max_value=20, step=0.5)

    # Bouton d'enregistrement
    submitted = st.form_submit_button("💾 Enregistrer")

    if submitted:
        if nom_prenom and module:  # Vérification que tout est bien rempli
            st.session_state.data.append([nom_prenom, module, note])
            st.success("✅ Note enregistrée avec succès !")
        else:
            st.warning("⚠️ Merci de remplir tous les champs avant d'enregistrer.")

# Convertir les données en DataFrame pour affichage
df = pd.DataFrame(st.session_state.data, columns=["Nom & Prénom", "Module", "Note finale"])

# Affichage des notes enregistrées
if not df.empty:
    st.write("📌 Voici toutes les entrées enregistrées :")
    st.dataframe(df)
else:
    st.write("ℹ️ Aucune entrée n'a encore été enregistrée.")
