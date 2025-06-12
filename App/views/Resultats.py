import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Annonces similaires")
st.write("Validez les annonces se rapprochant le plus du bien : ")
    # Appel du modèle NeighborFinder (à implémenter)
    # results = neighbor_finder_model.find(df, criteria)
    # st.write("Annonces similaires :", results)

df_ann = pd.DataFrame({
    "Nom de l'annonce": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
    "Lien de l'annonce": ["www.lien.com"]*4,
    "Surface (m²)": ['130', '140', '115', '145'],
    "...": ["..."]*4,
    "Prix de vente (€)": [100000, 132000, 120000, 200000],
    "Validation": [True, False, False, False]
})

st.write(edited_df = st.data_editor(df_ann, num_rows='dynamic'))

st.button("Valider les anonnces jumelles")

# Carte centrée sur la Côte Basque
m = folium.Map(location=[43.48333, -1.48333], zoom_start=12)
folium.Marker([43.48333, -1.48333], popup="Bayonne", tooltip="Bayonne").add_to(m)
st_folium(m, width=725)

st.write(pd.DataFrame({
    "Nom de l'annonce": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
    "Lien de l'annonce": ["www.lien.com"]*4,
    "Surface (m²)": ['130', '140', '115', '145'],
    "...": ["..."]*4,
    "Prix de vente (€)": [100000, 132000, 120000, 200000]
}))