import pandas as pd
import streamlit as st 
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
import folium

lien = "dataset_annonce_train.xlsx"
df = pd.read_excel(lien)

def acceuil() : 
    with st.sidebar:
        selection = option_menu(menu_title=None, options=["Acceuil", "DashBoard","Prédiction de vente"])
    
    if selection == "Acceuil":
        st.header("The BordishDashBoard")
        m = folium.Map(location=[43.48333, -1.48333], zoom_start=12)
        folium. Marker([43.48333, -1.48333], popup="Bayonne", tooltip="Bayonne").add_to(m)
        st_data = st_folium(m, width=725)

acceuil()