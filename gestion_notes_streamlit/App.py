import streamlit as st
import pandas as pd
import streamlit as st
import os

# Vérifier si l'image existe
image_path = "gestion_notes_streamlit/Logo.webp"

if os.path.exists(image_path):
    st.image(image_path, width=100)
else:
    st.error(f"L'image {image_path} est introuvable. Vérifiez le chemin et l'emplacement du fichier.")


# Centrage du logo
st.markdown(
    """
    <div style="text-align: center;">
        <img src="Logo.webp" width="100">
    </div>
    """,
    unsafe_allow_html=True
)

# Titre et message d'accueil
st.title("📚 Application de Gestion des Notes")
st.write("Veuillez remplir le formulaire ci-dessous pour enregistrer une note.")

# Initialisation de la session si nécessaire
if "data" not in st.session_state:
    st.session_state.data = []

# Formulaire pour l'ajout de notes
with st.form("formulaire_note"):
    nom_prenom = st.text_input("✍️ Nom & Prénom", placeholder="Entrez votre nom complet")
    module = st.text_input("📖 Module", placeholder="Ex : Mathématiques, Informatique...")
    note = st.number_input("🎯 Note finale", min_value=0.0, max_value=20.0, step=0.5)  # Correction ici !

    # 🔴 Ajout du bouton de soumission manquant
    submitted = st.form_submit_button("💾 Enregistrer")

    if submitted:
        if nom_prenom and module:
            st.session_state.data.append([nom_prenom, module, note])
            st.success("✅ Note enregistrée avec succès !")
        else:
            st.warning("⚠️ Merci de remplir tous les champs avant d'enregistrer.")

# Convertir en DataFrame et afficher les notes
df = pd.DataFrame(st.session_state.data, columns=["Nom & Prénom", "Module", "Note finale"])

if not df.empty:
    st.write("📌 Voici toutes les entrées enregistrées :")
    st.dataframe(df)
else:
    st.write("ℹ️ Aucune entrée n'a encore été enregistrée.")
