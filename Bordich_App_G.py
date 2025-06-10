import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import folium

# Chargement des données !!!!
lien = "dataset_annonce_train.xlsx"
df = pd.read_excel(lien)

account_d = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attemps": 0,
            "logged_in": "False",
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attemps": 0,
            "logged_in": "False",
            "role": "administrateur",
        },
    }
}

authenticator = Authenticate(account_d, "First_cookie", "cookie_key", 30)
authenticator.login()

# Fonction d'affichage du NeighborFinder
def neighbor_finder_page():
    st.title("Modèle trouvant les annonces les plus proches du bien à vendre")
    st.text(
        "Ici, après avoir inséré les caractéristiques du bien à vendre, le modèle donnera une liste d'annonces actives proposant des caractéristiques "
        "proches du bien du client : nb pièces, proximité plage, parking, classe énergétique, "
        "surface, type de bien, etc., sans prendre en compte le prix de vente."
    )

    # Formulaire de critères
    with st.form(key="property_form"):
        st.subheader("Entrez les caractéristiques du bien à vendre")

        # Localisation
        address = st.text_input("Adresse complète du bien", help="Permet de calculer les coordonnées géographiques")

        # Type et année de construction
        property_type = st.selectbox(
            "Type de bien", options=["Appartement", "Maison", "Studio", "Villa"]
        )
        construction_year = st.number_input(
            "Année de construction", min_value=1800, max_value=2025, value=2000, step=1
        )

        # Surface et pièces
        surface = st.number_input(
            "Surface habitable (m²)", min_value=10, max_value=500, value=80, step=1
        )
        land_surface = st.number_input(
            "Surface terrain (m²)", min_value=0, max_value=5000, value=0, step=10
        )
        nb_pieces = st.number_input(
            "Nombre de pièces", min_value=1, max_value=10, value=3, step=1
        )
        bedroom_count = st.number_input(
            "Nombre de chambres", min_value=0, max_value=10, value=2, step=1
        )

        # Étage
        floor = st.number_input(
            "Étage (numéro)", min_value=0, max_value=50, value=0, step=1,
            help="0 = rez-de-chaussée"
        )
        floor_count = st.number_input(
            "Nombre total d'étages", min_value=1, max_value=50, value=1, step=1
        )

        # Énergie et chauffage
        energy_class = st.selectbox(
            "Classe énergétique (DPE)", options=["A", "B", "C", "D", "E", "F", "G"]
        )
        heating_type = st.selectbox(
            "Type de chauffage", options=[
                "Balcon", "Terrasse", "Jardin", "Piscine", "Garage", "Parking extérieur", 
                "Parking couvert", "Cave", "Buanderie", "Cheminée", "Climatisation", 
                "Ascenseur", "Interphone", "Digicode", "Alarme", "Domotique", 
                "Accès PMR", "Vidéosurveillance", "Fibre optique"
            ]
        )
        heating_mode = st.selectbox(
            "Mode de chauffage", options=["Individuel", "Collectif"]
        )

        # Équipements / options
        options = st.multiselect(
            "Équipements (options)",
            options=["Balcon", "Ascenseur", "Parking extérieur", "Piscine", "Jardin", "Cave", "Terrasse"]
        )
        parking = st.checkbox("Parking disponible")

        submitted = st.form_submit_button("Trouver les annonces similaires")

    if submitted:
        # Géocodage de l'adresse
        latitude, longitude = geocode_address(address) if address else (None, None)

        criteria = {
            "address": address,
            "latitude": latitude,
            "longitude": longitude,
            "property_type": property_type,
            "construction_year": construction_year,
            "surface": surface,
            "land_surface": land_surface,
            "nb_pieces": nb_pieces,
            "bedroom_count": bedroom_count,
            "floor": floor,
            "floor_count": floor_count,
            "energy_class": energy_class,
            "heating_type": heating_type,
            "heating_mode": heating_mode,
            "options": options,
            "parking": parking,
        }
        st.image("https://i.etsystatic.com/11012956/r/il/9b5fb7/3870999220/il_fullxfull.3870999220_6vfu.jpg")
        # Appel du modèle NeighborFinder (à implémenter)
        # results = neighbor_finder_model.find(df, criteria)
        # st.write("Annonces similaires :", results)

    st.write("La suite à la prochaine page...")

# Fonction du tableau de résultats
def results_page():
    st.title("Vision globale des résultats du modèle")
    st.header("Résumé des caractéristiques des biens similaires sur Leboncoin")
    st.text("Exemples de données : durée de publication, prix moyen, etc.")
    
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


# Fonction d'étude de l'overpricing
def overpricing_page():
    st.title("Étude de l'overpricing sur le délai de vente")
    st.text(
        "Analyse de l'influence de la sur/sous cotation d'un bien sur le temps total de publication d'une annonce"
        "avec la moyenne du marché."
    )
    # À implémenter...

if st.session_state["authentication_status"]:
    # Barre de navigation
    PAGES = ["Acceuil", "NeighborFinder", "Résultats", "Overpricing"]
    with st.sidebar:
        selection = option_menu(menu_title=None, options=PAGES)
        authenticator.logout("Déconnexion")
        
    # Routing
    if selection == "Acceuil":
        st.title("Welcome to the..... BordishDashBoard")
        st.image(
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMm1wbmw4eGxvejU3emdmOTJhYmxmM3Q2dmNoZzE3Ym52NnVmcDkxMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g9582DNuQppxC/giphy.gif"
        )
        
    elif selection == "NeighborFinder":
        neighbor_finder_page()
    elif selection == "Résultats":
        results_page()
    elif selection == "Overpricing":
        overpricing_page()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.error("Les champs username et mot de passe doivent être remplie")

