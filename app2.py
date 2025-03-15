import streamlit as st
import pandas as pd

# Interface utilisateur
st.title("Surveillance NFS sous Méthotrexate")
st.write("Bienvenue sur l'application de surveillance des patients sous Méthotrexate")
st.set_page_config(page_title="Surveillance NFS", layout="wide")

# Entrée des données patient
patient_id = st.number_input("ID Patient", min_value=1, step=1)
Age = st.number_input("Age", min_value=1, step=1)
pathologie = st.selectbox("Pathologie", ["P.R", "Pso", "Lupus"])
Hb = st.number_input("Hémoglobine (g/dL)", min_value=5.0, max_value=20.0, step=0.1)
Gb = st.number_input("Globules blancs (G/L)", min_value=0.1, max_value=10.0, step=0.1)
pnn = st.number_input("PNN (G/L)", min_value=0.1, max_value=10.0, step=0.1)
Plaquettes = st.number_input("Plaquettes (G/L)", min_value=10, max_value=500, step=10)

#permet de définir un dico des alternatives spécifiées

alternatives = {
    "P.R": "Leflunomide",
    "Pso": "Biothérapie",
    "Lupus": "Mycophénolate mofétil"
}


if Gb < 3 or PNN < 1 or Plaquettes < 100:
    alternative = alternatives.get(pathologie, "Non spécifiée")
    st.error(f"⚠ Alerte Aplasie Médullaire ! Alternative recommandée : {alternative}")
else:
    st.success("✅ NFS normale, poursuite du traitement possible")  


